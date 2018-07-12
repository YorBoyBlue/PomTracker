from helpers.yaml_helper import YamlHelper


class ConfigMiddleware:
    def __init__(self):
        filepath = 'config/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        self.time_blocks = data.get('time_blocks')
        self.excluded_paths = ['/app/login', '/css/style.css',
                               '/css/user_create.css',
                               '/css/bootstrap.css',
                               '/css/bootstrap.css',
                               '/css/bootstrap.min.css',
                               '/css/bootstrap.min.css.map',
                               '/css/bootstrap-grid.css',
                               '/css/bootstrap-grid.css.map',
                               '/css/bootstrap-grid.min.css',
                               '/css/bootstrap-grid.min.css.map',
                               '/css/bootstrap-reboot.css',
                               '/css/bootstrap-reboot.css.map',
                               '/css/bootstrap-reboot.min.css',
                               '/css/bootstrap-reboot.min.css.map',
                               '/js/bootstrap.js',
                               '/js/bootstrap.min.js',
                               '/js/jquery.js',
                               '/assets/time.jpg'
                               ]

    def process_request(self, req, resp):
        req.context['time_blocks'] = self.time_blocks
        req.context['excluded_paths'] = self.excluded_paths
