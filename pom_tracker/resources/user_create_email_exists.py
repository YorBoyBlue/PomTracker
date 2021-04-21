from mako.template import Template


class UserCreateEmailExistsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_create_template = Template(filename='pom_tracker/views/user_create_view.mako')
        resp.body = user_create_template.render(
            email_exists=True
        )
