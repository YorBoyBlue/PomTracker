import falcon
import pytz
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.pomodora_model import PomodoraModel
from models.pom_flags_model import PomFlagsModel
from marshmallow import ValidationError
from models.pomodora_schema import PomodoraSchema


class PomodoraCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        today = datetime.utcnow().date()
        resp.content = req.context['session'].query(
            PomodoraModel).filter_by(created=today,
                                     user_id=req.context['user'].id).all()

    def on_post(self, req, resp):
        """Handles POST requests"""

        task = req.media.get('task', None)
        review = req.media.get('review', None)
        flags = req.media.get('flags', None)
        times = req.media['time_block'].split('-')
        start_time = datetime.strptime(times[0].strip(), '%I:%M%p').replace(
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

        try:
            PomodoraSchema().load(
                {'task': task, 'review': review, 'flags': flags})
        except ValidationError as err:
            message = err.messages  # => {'email': ['"foo" is not a valid email address.']}
            data = err.valid_data
            raise falcon.HTTPBadRequest(
                "You're missing some of the required fields.",
                data
            )

        else:
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

            # Try to add pom to the DB
            try:
                req.context['session'].add(pom_to_add)
                req.context['session'].commit()
            except IntegrityError as e:
                # Pomodora already exists with that time block
                req.context['session'].rollback()
                # Create dict with form data to send back to the browser
                formData = {
                    'distractions': distractions,
                    'pom_success': pom_success,
                    'review': review,
                    'task': task,
                    'time_block': times
                }
                raise falcon.HTTPBadRequest(formData)

            # Success! Let ajax reload the page
            resp.status = falcon.HTTP_200
