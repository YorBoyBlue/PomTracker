import falcon
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from mako.template import Template
from database.database_manager import dbm
from models.user_model import UserModel


class UserCreateResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_create_template = Template(filename='pom_tracker/views/user_create_view.mako')
        resp.text = user_create_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        db = dbm.get_db()

        # Add user to the DB
        email = req.get_param('email')
        first_name = req.get_param('first_name')
        middle_name = req.get_param('middle_name')
        last_name = req.get_param('last_name')
        display_name = req.get_param('display_name')
        password = req.get_param('password')
        today = datetime.utcnow()
        user_to_add = UserModel(
            email=email,
            first_name=first_name, middle_name=middle_name,
            last_name=last_name,
            display_name=display_name,
            password=password,
            created=today,
            modified=today
        )
        try:
            db.add(user_to_add)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            raise falcon.HTTPFound('/user/create_email_exists')

        else:
            # Send user to the login page if their account was created
            raise falcon.HTTPFound('/user/login')
