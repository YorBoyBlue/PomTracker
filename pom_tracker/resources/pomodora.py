import falcon
from helpers.yaml_helper import YamlHelper
from models.pomodora_model import PomodoraModel
import datetime


class PomodoraResource:

    def __init__(self):
        self.time_blocks = []
        self.init_times()

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        with open('views/pomodora_view.html', 'r') as f:
            resp.body = f.read()

    def on_post(self, req, resp):
        """Handles POST requests"""
        my_media = req.media

        # Add pom to the DB
        # times = pom.time_block.split('-')
        start_time = '9:00am'
        end_time = '9:25am'
        today = datetime.date.today()
        pom_to_add = PomodoraModel(task=req.media['task'],
                                   review=req.media['review'], date=today,
                                   start_time=start_time, end_time=end_time)
        req.context['session'].add(pom_to_add)
        req.context['session'].commit()

        # Redirect to pomodora page again
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        with open('views/pomodora_view.html', 'r') as f:
            resp.body = f.read()

    def init_times(self):
        filepath = 'templates/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        time_blocks = data.get('time_blocks')
        for val, time_block in time_blocks.items():
            self.time_blocks.append(time_block)
