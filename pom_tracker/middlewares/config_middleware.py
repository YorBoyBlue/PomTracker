from helpers.yaml_helper import YamlHelper


class ConfigMiddleware:
    def __init__(self):
        filepath = 'config/pom_sheet_times_template.yaml'
        data = YamlHelper().loader(filepath)
        self.time_blocks = data.get('time_blocks')
        self.excluded_paths_validate = [
            '/app/login',
            '/app/logout',
            '/app/create',
            '/app/create_email_exists',
            '/app/home',
            '/app/login_failed',
            '/app/session_expired',
            '/api/users',
            '/favicon.ico'
        ]
        self.excluded_folders_validate = [
            '/css/',
            '/js/',
            '/assets/'
        ]
        self.included_paths_user = [
            '/app/pomodora',
            '/api/poms',
            '/api/pom_sheet_export',
            '/app/export_poms',
            '/app/pom_exists',
            '/app/logout',
            '/api/pom_replace'
        ]

    def process_request(self, req, resp):
        req.context['time_blocks'] = self.time_blocks
        req.context['excluded_paths_validate'] = self.excluded_paths_validate
        req.context[
            'excluded_folders_validate'] = self.excluded_folders_validate
        req.context['included_paths_user'] = self.included_paths_user
