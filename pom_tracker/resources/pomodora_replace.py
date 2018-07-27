import falcon
import pytz
from datetime import datetime
from error_handling.my_exceptions import NoSessionRecordExists
from models.pomodora_model import PomodoraModel
from models.pom_flags_model import PomFlagsModel


class PomodoraReplaceResource:
    def on_post(self, req, resp):
        """Handles POST requests"""

        # Parse variables to be submitted to DB
        task = req.media.get('task', None)
        review = req.media.get('review', None)
        flags = req.media.get('flags', None)
        times = req.media['time_block'].split('-')
        start_time = datetime.strptime(times[0].strip(),
                                       '%I:%M%p').replace(
            tzinfo=pytz.UTC)
        end_time = datetime.strptime(times[1].strip(), '%I:%M%p').replace(
            tzinfo=pytz.UTC)
        today = datetime.utcnow().date()
        user_id = req.context['user'].id
        was_distractions = req.media.get('distractions', 0)
        distractions = 0
        if was_distractions:
            for distraction in req.media['distractions']:
                distractions += 1
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

        # Create pomodora model object to submit to DB
        pom_to_add = PomodoraModel(user_id=user_id,
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
            records_updated_count = req.context['session'].query(
                PomodoraModel).filter_by(user_id=user_id).update(
                pom_to_add)
            req.context['session'].update(pom_to_add)
            if records_updated_count == 0:
                raise NoSessionRecordExists(
                    'No session for this user was found')

            req.context['session'].commit()

            # create a new session in DB if one does not exist
        except NoSessionRecordExists as e:
            data = {
                'form_data': form_data,
                'message': '<br> * If this error message is shown I need '
                           'to handle it properly.'
            }

            raise falcon.HTTPBadRequest(
                {
                    'error': 'PomExistsError',
                    'data': data
                }
            )

        # Success! Let js ajax reload the page
        resp.status = falcon.HTTP_200
