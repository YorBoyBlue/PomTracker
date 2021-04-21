from yaml import safe_load


class ConfigMiddleware:
    def __init__(self):
        self.time_blocks = self.get_time_block_data()
        self.excluded_paths_validate = [
            '/home',
            '/user/login',
            '/user/logout',
            '/user/create',
            '/user/create_email_exists',
            '/user/login_failed',
            '/user/session_expired',
            '/favicon.ico'
        ]
        self.excluded_folders_validate = [
            '/assets/'
        ]
        self.included_paths_user = [
            '/user/logout',
            '/pomodoro',
            '/app/poms/today',
            '/app/poms',
            '/app/pom_sheet_export',
            '/app/export_poms',
            '/app/pom_exists'
        ]

    def process_request(self, req, resp):
        req.context['time_blocks'] = self.time_blocks
        req.context['excluded_paths_validate'] = self.excluded_paths_validate
        req.context['excluded_folders_validate'] = self.excluded_folders_validate
        req.context['included_paths_user'] = self.included_paths_user

    def get_time_block_data(self):
        filepath = 'pom_tracker/config/pom_sheet_times_template.yaml'
        with open(filepath, 'r') as f:
            time_block_data = safe_load(f)
        return time_block_data.get('time_blocks')
