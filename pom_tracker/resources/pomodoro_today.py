import falcon
from resources.resourse_base import ResourceBase
from mako.template import Template
from controllers.pomodoro import get_today, get_flag_types, validate, insert_poms


class PomodoroTodayResource(ResourceBase):

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

        user_id = req.context['user'].id
        post = req.get_media()

        # Parse POST variables to be submitted to DB
        task = self.get_param(post.get('task'))
        review = self.get_param(post.get('review'))
        pom_success = self.get_param(post.get('pom_success'), default=0)
        flags = self.get_param_as_list(post.get('flags'))
        time_blocks = self.get_param_as_list(post.get('time_block'))
        distractions = self.get_param_as_list(post.get('distractions'))
        distractions_count = len(distractions) if distractions else 0

        # Validate pomodoro
        validated = validate(task, review, flags, time_blocks)
        if not validated.get('validated'):
            raise falcon.HTTPBadRequest(
                {
                    'error': 'ValidationError',
                    'message': validated.get('message', '<br>Something unexpected happened.')
                }
            )

        success = insert_poms(
            user_id,
            task,
            review,
            flags,
            distractions_count,
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
