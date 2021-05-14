import falcon
from ..resources.resourse_base import ResourceBase
from ..controllers.user import get_user, login_user

from mako.template import Template
from sqlalchemy.orm.exc import NoResultFound
import random
import string
import hashlib


class UserLoginResource(ResourceBase):
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/user_login_view.mako')
        resp.text = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        post = req.get_media()

        # Parse POST variables
        email = self.get_param(post.get('email'))
        password = self.get_param(post.get('password'))

        # Validate user
        try:
            user = get_user(email)

        # User was not found, send back to login failed end point
        except NoResultFound as e:
            raise falcon.HTTPFound('/user/login_failed')

        # User email is validated. Validate password as well
        else:

            # User is validated, create or modify existing session for the user
            if user.password == password:
                user_id = user.id
                rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
                hash_object = hashlib.md5(rand_string.encode())
                pomodoro_login_hash = hash_object.hexdigest()

                login_user(user_id, pomodoro_login_hash)

                resp.set_cookie('pomodoro_login_hash', pomodoro_login_hash,
                                max_age=79200, path='/')
                raise falcon.HTTPFound('/pomodoro/today')

            else:
                raise falcon.HTTPFound('/user/login_failed')
