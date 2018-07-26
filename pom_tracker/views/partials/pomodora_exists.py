import os
from helpers.my_requests import Requests
from mako.template import Template
from resources.flag_types import FlagTypesResource


class PomodoraExistsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        # Simulated downstream request
        Requests().get(req, resp, FlagTypesResource())
        flag_types = resp.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        pomodora_template = Template(
            filename=dir_path + '/pomodora_exists_view.mako')
        resp.body = pomodora_template.render(
            time_blocks=req.context['time_blocks'],
            flag_types=flag_types,
            time_block=req.params.get('time_block'),
            flags=req.params.get('flags'),
            task=req.params.get('task'),
            review=req.params.get('review'),
            distractions=req.params.get('distractions'),
            pom_success=req.params.get('pom_success')
        )
