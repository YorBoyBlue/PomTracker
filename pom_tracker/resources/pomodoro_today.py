import falcon
from mako.template import Template
from controllers.pomodoro import get_today, get_flag_types, validate, insert_poms


class PomodoroTodayResource:

    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        todays_poms = get_today(req.context['user'].id)
        flag_types = get_flag_types()

        pomodoro_template = Template(filename='pom_tracker/views/pomodoro_view.mako')
        resp.text = pomodoro_template.render(
            time_blocks=req.context['time_blocks'],
            pom_rows=todays_poms,
            flag_types=flag_types
        )

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Parse variables to be submitted to DB
        task = req.get_param('task')
        review = req.get_param('review')
        flags = req.get_param_as_list('flags')
        time_blocks = req.get_param_as_list('time_block')

        # Validate pomodoro
        validated = validate(task, review, flags, time_blocks)
        if not validated.get('validated', False):
            raise falcon.HTTPBadRequest(
                {
                    'error': 'ValidationError',
                    'message': validated.get('message', '<br>Something unexpected happened.')
                }
            )

        user_id = req.context['user'].id
        was_distractions = req.get_param('distractions', default=0)
        distractions = 0
        if was_distractions:
            for distraction in req.get_param_as_list('distractions'):
                distractions += 1
        pom_success = req.get_param('pom_success', default=0)
        time_blocks = req.get_param_as_list('time_block')

        success = insert_poms(
            user_id,
            task,
            review,
            flags,
            distractions,
            pom_success,
            time_blocks
        )

        if not success:
            raise falcon.HTTPBadRequest(
                {
                    'error': 'PomExistsError',
                    'message': '<br>You have already submitted a pomodoro today with one of the '
                               'selected time blocks. Pick another time block and resubmit.'
                }
            )

        # Success! Let js ajax send user to submit the pom
        resp.status = falcon.HTTP_200
