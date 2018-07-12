import falcon
import os
from mako.template import Template


class UserCreateResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        user_create_template = Template(
            filename=dir_path + '/user_create_view.mako')
        resp.body = user_create_template.render()
