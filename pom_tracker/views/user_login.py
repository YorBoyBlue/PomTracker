import falcon
import os
from error_handling.my_exceptions import NoSessionRecordExists
from mako.template import Template
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from models.session_model import SessionModel
from models.user_model import UserModel
import random
import string
import hashlib


class UserLoginResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        user_login_template = Template(
            filename=dir_path + '/user_login_view.mako')
        resp.body = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Validate user
        try:
            user = req.context['session'].query(
                UserModel).filter_by(email=req.media['email']).one()

        # User was not found, send back to login failed end point
        except NoResultFound as e:
            raise falcon.HTTPFound('/app/login_failed')

        # User email is validated. Validate password as well
        else:
            # User is validated, create or modify existing session for the user
            if user.password == req.media['password']:
                rand_string = ''.join(
                    random.choices(string.ascii_uppercase + string.digits,
                                   k=20))
                hash_object = hashlib.md5(rand_string.encode())
                pomodora_login_hash = hash_object.hexdigest()
                now = datetime.utcnow()
                # check if user has an existing session in DB and modify it
                try:
                    records_updated_count = req.context['session'].query(
                        SessionModel).filter_by(user_id=user.id).update(
                        {"hash": pomodora_login_hash,
                         "modified": now
                         })

                    if records_updated_count == 0:
                        raise NoSessionRecordExists(
                            'No session for this user was found')

                    req.context['session'].commit()

                # create a new session in DB if one does not exist
                except NoSessionRecordExists as e:
                    session_to_add = SessionModel(user_id=user.id,
                                                  hash=pomodora_login_hash,
                                                  created=now, modified=now)
                    req.context['session'].add(session_to_add)
                    req.context['session'].commit()

                # Send user to the pomodora page
                finally:
                    resp.set_cookie('pomodora_login_hash', pomodora_login_hash,
                                    max_age=88200, path='/')
                    raise falcon.HTTPFound('/app/pomodora')

            else:
                raise falcon.HTTPFound('/app/login_failed')
