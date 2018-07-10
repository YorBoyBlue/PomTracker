import falcon
from models.pomodora_model import PomodoraModel
from models.pom_flags_model import PomFlagsModel
from datetime import datetime, date
from sqlalchemy.exc import IntegrityError


class PomodoraCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        today = date.today()
        resp.content = req.context['session'].query(
            PomodoraModel).filter_by(add_date=today).all()

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Add pom to the DB
        times = req.media['time_block'].split('-')
        start_time = datetime.strptime(times[0], '%I:%M%p')
        end_time = datetime.strptime(times[1], '%I:%M%p')
        today = date.today()
        pom_to_add = PomodoraModel(task=req.media['task'],
                                   review=req.media['review'], add_date=today,
                                   start_time=start_time.time(),
                                   end_time=end_time.time())
        for flag in req.media['flags']:
            pom_to_add.flags.append(PomFlagsModel(flag_type=flag))
        try:
            req.context['session'].add(pom_to_add)
            req.context['session'].commit()
        except IntegrityError as e:
            # Insert failed due to a unique constraint
            # TODO: create a pop up to let the user know there is a pom with
            # TODO: that time block already and ask if they want to replace it.
            req.context['session'].rollback()
            message = 'You already have a pom for that time block. Delete ' \
                      'it if you want to add a new one.'
            e.statement = message

        # Send user to pomodora page again
        raise falcon.HTTPFound('/app/pomodora')
