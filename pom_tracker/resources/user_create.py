import falcon
from ..resources.resourse_base import ResourceBase
from mako.template import Template
from ..controllers.user import create_user


class UserCreateResource(ResourceBase):
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_create_template = Template(filename='pom_tracker/views/user_create_view.mako')
        resp.text = user_create_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""
        post = req.get_media()

        # Parse POST variables
        email = self.get_param(post.get('email'))
        first_name = self.get_param(post.get('first_name'))
        middle_name = self.get_param(post.get('middle_name'))
        last_name = self.get_param(post.get('last_name'))
        display_name = self.get_param(post.get('display_name'))
        password = self.get_param(post.get('password'))

        success = create_user(email, first_name, middle_name, last_name, display_name, password)

        if not success:
            raise falcon.HTTPFound('/user/create_email_exists')
        else:
            # Send user to the login page if their account was created
            raise falcon.HTTPFound('/user/login')
