from mako.template import Template


class UserSettingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/user_settings_view.mako')
        resp.body = user_login_template.render()
