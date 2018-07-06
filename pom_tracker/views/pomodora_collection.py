import falcon
from models.pomodora_model import PomodoraModel
import datetime
from mako.template import Template
from helpers.yaml_helper import YamlHelper


class PomodoraCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        today = datetime.date.today()
        resp.content = req.context['session'].query(
            PomodoraModel).filter_by(date=today).all()

    def on_post(self, req, resp):
        """Handles POST requests"""

        # Add pom to the DB
        times = req.media['time_block'].split('-')
        start_time = times[0]
        end_time = times[1]
        today = datetime.date.today()
        pom_to_add = PomodoraModel(task=req.media['task'],
                                   review=req.media['review'], date=today,
                                   start_time=start_time, end_time=end_time)
        req.context['session'].add(pom_to_add)
        req.context['session'].commit()

        # Send user to pomodora page again
        raise falcon.HTTPFound('/pomodora')
