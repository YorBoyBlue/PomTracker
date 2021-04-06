import falcon
from marshmallow import ValidationError
from models.pomodoro_schema import PomodoroSchema


class PomodoroValidationResource:

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Parse variables to be submitted to DB
        task = req.get_param('task')
        review = req.get_param('review')
        flags = req.get_param_as_list('flags')
        time_blocks = req.get_param_as_list('time_block')

        # Store form data that came in from the user
        form_data = {
            'distractions': req.get_param('distractions'),
            'pom_success': req.get_param('pom_success', default=0),
            'review': review,
            'task': task,
            'flags': flags,
            'selected_time_blocks': time_blocks
        }

        # Validate form
        try:
            PomodoroSchema().load(
                {'task': task, 'review': review, 'flags': flags})
        except ValidationError as err:
            # User is missing 1 or more required fields
            message = ''
            for k, v in err.messages.items():
                message += '<br> * ' + v[0]
            data = {
                'form_data': form_data,
                'message': message
            }
            raise falcon.HTTPBadRequest(
                {
                    'error': 'ValidationError',
                    'data': data
                }
            )

        else:
            raise falcon.HTTPFound('/api/poms/today')
