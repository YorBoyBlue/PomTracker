import falcon
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.user_model import UserModel


class UserCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.content = req.context['session'].query(
            UserModel).filter_by(email=req.get_param('email'))

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Add user to the DB
        email = req.get_param('email')
        first_name = req.get_param('first_name')
        middle_name = req.get_param('middle_name')
        last_name = req.get_param('last_name')
        display_name = req.get_param('display_name')
        password = req.get_param('password')
        today = datetime.utcnow()
        user_to_add = UserModel(email=email,
                                first_name=first_name, middle_name=middle_name,
                                last_name=last_name,
                                display_name=display_name,
                                password=password,
                                created=today,
                                modified=today)
        try:
            req.context['session'].add(user_to_add)
            req.context['session'].commit()
        except IntegrityError as e:
            req.context['session'].rollback()
            raise falcon.HTTPFound('/app/create_email_exists')

        else:
            # Send user to the login page if their account was created
            raise falcon.HTTPFound('/app/login')
