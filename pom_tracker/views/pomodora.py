import falcon
from mako.template import Template
from helpers.yaml_helper import YamlHelper
from resources.pomodora_collection import PomodoraCollectionResource


class PomodoraResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'

        # TODO: Create a fake request lib to handle resource specific requests
        # Simulated downstream request
        request = PomodoraCollectionResource()
        request.on_get(req, resp)
        collection_of_poms = resp.content  # This has my collection

        pomodora_template = Template(
            filename=
            'C:/Work/Python/PomTracker/pom_tracker/views/pomodora_view.mako')
        # resp.body = pomodora_template.render(time_blocks=self.init_times())
        resp.body = pomodora_template.render(time_blocks=self.init_times(),
                                             pom_rows=collection_of_poms)

    # TODO: Create a config lib to store data once on app start rather then every request
    @staticmethod
    def init_times():
        filepath = 'templates/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        return data.get('time_blocks')
