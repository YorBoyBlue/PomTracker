import falcon
import pytz
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.pomodoro_model import PomodoroModel
from models.pom_flags_model import PomFlagsModel


class PomodoroCollectionTodayResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        today = datetime.now().date()
        resp.content = req.context['session'].query(
            PomodoroModel).filter_by(created=today,
                                     user_id=req.context['user'].id).all()

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Parse variables to be submitted to DB
        task = req.get_param('task')
        review = req.get_param('review')
        flags = req.get_param_as_list('flags')
        today = datetime.now().date()
        user_id = req.context['user'].id
        was_distractions = req.get_param('distractions', default=0)
        distractions = 0
        if was_distractions:
            for distraction in req.get_param_as_list('distractions'):
                distractions += 1
        pom_success = req.get_param('pom_success', default=0)
        time_blocks = req.get_param_as_list('time_block')

        # Store form data that came in from the user
        form_data = {
            'distractions': req.get_param('distractions'),
            'pom_success': pom_success,
            'review': review,
            'task': task,
            'flags': flags,
            'selected_time_blocks': time_blocks
        }

        for time_block in time_blocks:

            times = time_block.split('-')

            start_time = datetime.strptime(times[0].strip(), '%I:%M%p').replace(
                tzinfo=pytz.UTC)
            end_time = datetime.strptime(times[1].strip(), '%I:%M%p').replace(
                tzinfo=pytz.UTC)

            # Create pomodoro model object to submit to DB
            pom_to_add = PomodoroModel(user_id=user_id,
                                       distractions=distractions,
                                       pom_success=pom_success,
                                       task=task,
                                       review=review, created=today,
                                       start_time=start_time.time(),
                                       end_time=end_time.time())
            for flag in flags:
                pom_to_add.flags.append(PomFlagsModel(flag_type=flag))

            # Add pom to the DB
            try:
                req.context['session'].add(pom_to_add)
                req.context['session'].commit()
            except IntegrityError as e:
                # Pomodoro already exists with that time block
                req.context['session'].rollback()
                # Create dict with form data to send back to the browser
                data = {
                    'form_data': form_data,
                    'message': '<br> * You have already submitted a pomodoro '
                               'with that start time today. Pick another or '
                               'resubmit to replace the current pomodoro with '
                               'the new one.'
                }

                raise falcon.HTTPBadRequest(
                    {
                        'error': 'PomExistsError',
                        'data': data
                    }
                )

        # Success! Let js ajax send user to submit the pom
        resp.status = falcon.HTTP_200
