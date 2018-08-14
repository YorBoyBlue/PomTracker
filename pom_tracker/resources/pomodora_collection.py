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
        was_distractions = req.media.get('distractions', 0)
        distractions = 0
        if was_distractions:
            for distraction in req.media['distractions']:
                distractions += 1
        pom_success = req.media.get('pom_success', 0)
        pom_to_add = PomodoraModel(user_id=user_id, distractions=distractions,
                                   pom_success=pom_success,
                                   task=req.media['task'],
                                   review=req.media['review'], created=today,
                                   start_time=start_time.time(),
                                   end_time=end_time.time())
        for flag in req.media['flags']:
            pom_to_add.flags.append(PomFlagsModel(flag_type=flag))
        try:
            req.context['session'].add(pom_to_add)
            req.context['session'].commit()
        except IntegrityError as e:
            req.context['session'].rollback()
            raise falcon.HTTPFound('/app/pom_exists')

        # Send user to pomodora page again
        raise falcon.HTTPFound('/app/pomodora')