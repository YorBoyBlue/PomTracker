import os
from mako.template import Template


class UserCreateEmailExistsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        user_create_template = Template(
            filename=dir_path + '/user_create_view.mako')
        resp.body = user_create_template.render(
            email_exists=True
        )
