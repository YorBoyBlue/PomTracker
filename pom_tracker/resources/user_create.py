import falcon
from mako.template import Template
from controllers.user import create_user


class UserCreateResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_create_template = Template(filename='pom_tracker/views/user_create_view.mako')
        resp.text = user_create_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        email = req.get_param('email')
        first_name = req.get_param('first_name')
        middle_name = req.get_param('middle_name')
        last_name = req.get_param('last_name')
        display_name = req.get_param('display_name')
        password = req.get_param('password')

        success = create_user(email, first_name, middle_name, last_name, display_name, password)

        if not success:
            raise falcon.HTTPFound('/user/create_email_exists')
        else:
            # Send user to the login page if their account was created
            raise falcon.HTTPFound('/user/login')
