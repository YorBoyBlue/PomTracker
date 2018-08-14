import os
from mako.template import Template


class PomodoroSetResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        dir_path = os.path.dirname(os.path.realpath(__file__))
        pomodoro_template = Template(
            filename=dir_path + '/pomodoro_set_view.mako')
        resp.body = pomodoro_template.render()
