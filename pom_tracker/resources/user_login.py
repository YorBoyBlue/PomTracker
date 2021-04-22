import falcon
from error_handling.my_exceptions import NoSessionRecordExists
from mako.template import Template
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from models.session_model import SessionModel
from models.user_model import UserModel
from database.database_manager import dbm
import random
import string
import hashlib


class UserLoginResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/user_login_view.mako')
        resp.text = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        db = dbm.get_db()

        # Validate user
        try:
            email = req.get_param('email')
            user = db.query(UserModel).filter_by(email=email).one()

        # User was not found, send back to login failed end point
        except NoResultFound as e:
            raise falcon.HTTPFound('/user/login_failed')

        # User email is validated. Validate password as well
        else:
            # User is validated, create or modify existing session for the user
            if user.password == req.get_param('password'):
                rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
                hash_object = hashlib.md5(rand_string.encode())
                pomodoro_login_hash = hash_object.hexdigest()
                now = datetime.utcnow()
                # Check if user has an existing session in DB and modify it
                try:
                    records_updated_count = db.query(SessionModel).filter_by(
                        user_id=user.id).update({"hash": pomodoro_login_hash, "modified": now})

                    if records_updated_count == 0:
                        raise NoSessionRecordExists(
                            'No session for this user was found')

                    db.commit()

                # Create a new session in DB if one does not exist
                except NoSessionRecordExists as e:
                    session_to_add = SessionModel(user_id=user.id,
                                                  hash=pomodoro_login_hash,
                                                  created=now, modified=now)
                    db.add(session_to_add)
                    db.commit()

                # Send user to the pomodoro page
                finally:
                    resp.set_cookie('pomodoro_login_hash', pomodoro_login_hash,
                                    max_age=79200, path='/')
                    raise falcon.HTTPFound('/pomodoro/today')

            else:
                raise falcon.HTTPFound('/user/login_failed')
