from mako.template import Template
from controllers.pomodoro import get_flag_types


class PomodoroValidationErrorResource:

    def on_post(self, req, resp):
        """Handles POST requests"""

        resp.content_type = 'text/html'

        flag_types = get_flag_types()
        form_data = req.media.get('form_data')
        pomodoro_template = Template(
            filename='pom_tracker/views/partials/pomodoro_validation_error_view.mako')

        resp.body = pomodoro_template.render(
            time_blocks=req.context['time_blocks'],
            flag_types=flag_types,
            selected_time_blocks=form_data.get('selected_time_blocks'),
            flags=form_data.get('flags'),
            task=form_data.get('task'),
            review=form_data.get('review'),
            distractions=form_data.get('distractions'),
            pom_success=form_data.get('pom_success'),
            message=req.media.get('message')
        )
