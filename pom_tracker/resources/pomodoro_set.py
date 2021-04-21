from mako.template import Template


class PomodoroSetResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        pomodoro_template = Template(filename='pom_tracker/views/pomodoro_set_view.mako')
        resp.body = pomodoro_template.render()
