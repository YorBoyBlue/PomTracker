import falcon
import pytz
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.pomodora_model import PomodoraModel
from models.pom_flags_model import PomFlagsModel


class PomodoraCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        today = datetime.utcnow().date()
        resp.content = req.context['session'].query(
            PomodoraModel).filter_by(created=today,
                                     user_id=req.context['user'].id).all()

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Add pom to the DB
        times = req.media['time_block'].split('-')
        start_time = datetime.strptime(times[0].strip(), '%I:%M%p').replace(
            tzinfo=pytz.UTC)
        end_time = datetime.strptime(times[1].strip(), '%I:%M%p').replace(
            tzinfo=pytz.UTC)
        today = datetime.utcnow().date()
        user_id = req.context['user'].id
        pom_to_add = PomodoraModel(user_id=user_id, task=req.media['task'],
                                   review=req.media['review'], created=today,
                                   start_time=start_time.time(),
                                   end_time=end_time.time())
        for flag in req.media['flags']:
            pom_to_add.flags.append(PomFlagsModel(flag_type=flag))
        try:
            req.context['session'].add(pom_to_add)
            req.context['session'].commit()
        except IntegrityError as e:
            # Insert failed due to a unique constraint on
            # created/start_time/user_id
            # TODO: create a pop up to let the user know there is a pom with
            # TODO: that time block already and ask if they want to replace it.
            req.context['session'].rollback()
            message = 'You already have a pom for that time block. Delete ' \
                      'it if you want to add a new one.'
            e.statement = message

        # Send user to pomodora page again
        raise falcon.HTTPFound('/app/pomodora')
