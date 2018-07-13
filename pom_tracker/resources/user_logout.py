import falcon


class UserLogoutResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        cookies = req.cookies
        if 'pomodora_login_hash' in cookies:
            resp.unset_cookie('pomodora_login_hash')
            raise falcon.HTTPFound('/app/login')
