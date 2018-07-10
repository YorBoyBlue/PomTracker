import falcon
import os
from helpers.my_requests import Requests
from mako.template import Template
from resources.pomodora_collection import PomodoraCollectionResource
from resources.flag_types import FlagTypesResource


class PomodoraResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'

        # Simulated downstream request
        todays_poms = Requests().get(req, resp, PomodoraCollectionResource())
        flag_types = Requests().get(req, resp, FlagTypesResource())
        dir_path = os.path.dirname(os.path.realpath(__file__))
        pomodora_template = Template(
            filename=dir_path + '/pomodora_view.mako')
        resp.body = pomodora_template.render(
            time_blocks=req.context['time_blocks'],
            pom_rows=todays_poms,
            flag_types=flag_types)
