import falcon
import os
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

        resp.status = falcon.HTTP_200  # This is the default status
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
            # TODO: create and then send back to login failed end point
            raise falcon.HTTPFound('/app/create')

        # User is validated, create a session for that user
        else:
            if user.password == req.media['password']:
                rand_string = ''.join(
                    random.choices(string.ascii_uppercase + string.digits,
                                   k=20))
                hash_object = hashlib.md5(rand_string.encode())
                my_hash = hash_object.hexdigest()
                # check if user has an existing session in DB and modify it
                try:
                    req.context['session'].query(SessionModel).filter_by(
                        user_id=user.id).update(
                        {"hash": my_hash})
                    req.context['session'].commit()

                # create a new session in DB if one does not exist
                except NoResultFound as e:


                    now = datetime.utcnow()
                    session_to_add = SessionModel(user_id=user.id,
                                                  hash=my_hash,
                                                  create_date=now)
                    req.context['session'].add(session_to_add)
                    req.context['session'].commit()

                # Send user to the pomodora page
                finally:
                    resp.set_cookie('my_hash', my_hash, max_age=7200)
                    raise falcon.HTTPFound('/app/pomodora')

            else:
                raise falcon.HTTPFound('/app/login')
