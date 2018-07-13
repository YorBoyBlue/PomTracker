import os
from helpers.my_requests import Requests
from mako.template import Template
from resources.pomodora_collection import PomodoraCollectionResource
from resources.flag_types import FlagTypesResource


class PomodoraResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        # Simulated downstream request
        Requests().get(req, resp, PomodoraCollectionResource())
        todays_poms = resp.content
        Requests().get(req, resp, FlagTypesResource())
        flag_types = resp.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        pomodora_template = Template(
            filename=dir_path + '/pomodora_view.mako')
        resp.body = pomodora_template.render(
            time_blocks=req.context['time_blocks'],
            pom_rows=todays_poms,
            flag_types=flag_types)
