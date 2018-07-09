import falcon
from models.pomodora_model import PomodoraModel
from datetime import datetime, date

from helpers.yaml_helper import YamlHelper


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
        req.context['session'].add(pom_to_add)
        req.context['session'].commit()

        # Send user to pomodora page again
        raise falcon.HTTPFound('/app/pomodora')

    def get_todays_poms(self, req):
        today = date.today()
        return req.context['session'].query(
            PomodoraModel).filter_by(add_date=today).all()
