import falcon
from ..controllers.user import logout_user


class UserLogoutResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        cookies = req.cookies
        user_id = req.context['user'].id
        if 'pomodoro_login_hash' in cookies:
            # This will remove the cookie because we are overriding the existing one with a
            # negative max_age
            resp.set_cookie('pomodoro_login_hash', '', max_age=-1, path='/')
            logout_user(user_id)

        raise falcon.HTTPFound('/user/login')
