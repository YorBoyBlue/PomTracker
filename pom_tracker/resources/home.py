from mako.template import Template


class HomeResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/home_view.mako')
        resp.text = user_login_template.render()
