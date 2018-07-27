import os
from helpers.my_requests import Requests
from mako.template import Template
from resources.flag_types import FlagTypesResource


class PomodoraExistsErrorResource:

    def on_post(self, req, resp):
        """Handles POST requests"""

        resp.content_type = 'text/html'

        # Simulated downstream request
        Requests().get(req, resp, FlagTypesResource())
        flag_types = resp.content
        dir_path = os.path.dirname(os.path.realpath(__file__))
        form_data = req.media.get('form_data')
        pomodora_template = Template(
            filename=dir_path + '/pomodora_exists_error_view.mako')
        resp.body = pomodora_template.render(
            time_blocks=req.context['time_blocks'],
            flag_types=flag_types,
            time_block=form_data.get('time_block'),
            flags=form_data.get('flags'),
            task=form_data.get('task'),
            review=form_data.get('review'),
            distractions=form_data.get('distractions'),
            pom_success=form_data.get('pom_success'),
            message=req.media.get('message')
        )
