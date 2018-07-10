from helpers.yaml_helper import YamlHelper


class ConfigMiddleware:
    def __init__(self):
        filepath = 'config/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        self.time_blocks = data.get('time_blocks')

    def process_request(self, req, resp):
        req.context['time_blocks'] = self.time_blocks
