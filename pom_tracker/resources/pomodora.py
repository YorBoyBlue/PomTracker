import falcon
from models.pomodora_model import PomodoraModel
import datetime
from mako.template import Template
from helpers.yaml_helper import YamlHelper


class PomodoraResource:

    def __init__(self):
        pass
        # self.time_blocks = []

    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'

        pomodora_template = Template(
            filename=
            'C:/Work/Python/PomTracker/pom_tracker/views/pomodora_view.html')
        resp.body = pomodora_template.render(time_blocks=self.init_times())

    def on_post(self, req, resp):
        """Handles POST requests"""
        d = req.media

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
        resp.context['time_blocks'] = self.init_times()
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        pomodora_template = Template(
            filename=
            'C:/Work/Python/PomTracker/pom_tracker/views/pomodora_view.html')
        resp.body = pomodora_template.render(time_blocks=self.init_times())


    @staticmethod
    def init_times():
        times = tuple()
        filepath = 'templates/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        time_blocks = data.get('time_blocks')
        for val, time_block in time_blocks.items():
            times = times + (
                '<option>' + time_block + '</option>',)
        return times
