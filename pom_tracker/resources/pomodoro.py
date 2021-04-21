from mako.template import Template
from controllers.pomodoro import get_flag_types, get_todays_poms


class PomodoroResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        todays_poms = get_todays_poms(req.context['user'].id)
        flag_types = get_flag_types()

        pomodoro_template = Template(filename='pom_tracker/views/pomodoro_view.mako')
        resp.body = pomodoro_template.render(
            time_blocks=req.context['time_blocks'],
            pom_rows=todays_poms,
            flag_types=flag_types
        )
