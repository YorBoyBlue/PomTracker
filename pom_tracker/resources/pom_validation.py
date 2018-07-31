import falcon
from marshmallow import ValidationError
from models.pomodoro_schema import PomodoroSchema


class PomodoroValidationResource:

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Parse variables to be submitted to DB
        task = req.media.get('task', None)
        review = req.media.get('review', None)
        flags = req.media.get('flags', None)
        pom_success = req.media.get('pom_success', 0)

        # Store form data that came in from the user
        form_data = {
            'distractions': req.media.get('distractions'),
            'pom_success': pom_success,
            'review': review,
            'task': task,
            'flags': flags,
            'time_block': req.media['time_block']
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
