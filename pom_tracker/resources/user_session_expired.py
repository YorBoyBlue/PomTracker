from mako.template import Template


class UserSessionExpiredResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/user_login_view.mako')
        resp.text = user_login_template.render(session_expired=True)
