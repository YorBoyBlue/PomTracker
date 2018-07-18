import falcon


class UserLogoutResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        cookies = req.cookies
        if 'pomodora_login_hash' in cookies:
            # This will remove the cookie because we are overriding the
            # existing one with a negative max_age
            resp.set_cookie('pomodora_login_hash', '', max_age=-1, path='/')
        raise falcon.HTTPFound('/app/login')
