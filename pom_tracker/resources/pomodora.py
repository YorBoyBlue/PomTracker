import falcon
import requests
from mako.template import Template
from helpers.yaml_helper import YamlHelper
from models.pomodora_model import PomodoraModel
import datetime


class PomodoraResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        # r = requests.get('https://localhost:8000/submitPom')
        poms = self.get_todays_poms(req)
        pomodora_template = Template(
            filename=
            'C:/Work/Python/PomTracker/pom_tracker/views/pomodora_view.mako')
        # resp.body = pomodora_template.render(time_blocks=self.init_times())
        resp.body = pomodora_template.render(time_blocks=self.init_times(),
                                             pom_rows=poms)

    @staticmethod
    def init_times():
        filepath = 'templates/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        return data.get('time_blocks')

    def get_todays_poms(self, req):
        today = datetime.date.today()
        return req.context['session'].query(
            PomodoraModel).filter_by(date=today).all()
