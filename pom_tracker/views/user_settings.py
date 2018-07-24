import os
from mako.template import Template


class UserSettingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        user_login_template = Template(
            filename=dir_path + '/user_settings_view.mako')
        resp.body = user_login_template.render()
