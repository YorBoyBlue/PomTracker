import os
from helpers.my_requests import Requests
from mako.template import Template
from resources.pomodoro_collection_today import PomodoroCollectionTodayResource
from resources.flag_types import FlagTypesResource


class PomodoroResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'
        # resp.responseType = 'document'

        # Simulated downstream request
        Requests().get(req, resp, PomodoroCollectionTodayResource())
        todays_poms = resp.content
        Requests().get(req, resp, FlagTypesResource())
        flag_types = resp.content

        dir_path = os.path.dirname(os.path.realpath(__file__))
        pomodoro_template = Template(filename=dir_path + '/pomodoro_view.mako')
        resp.body = pomodoro_template.render(time_blocks=req.context['time_blocks'],
                                             pom_rows=todays_poms, flag_types=flag_types)
