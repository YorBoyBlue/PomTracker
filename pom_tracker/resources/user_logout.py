import falcon
from models.session_model import SessionModel


class UserLogoutResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        cookies = req.cookies
        if 'pomodora_login_hash' in cookies:
            # This will remove the cookie because we are overriding the
            # existing one with a negative max_age
            resp.set_cookie('pomodora_login_hash', '', max_age=-1, path='/')
            req.context['session'].query(
                SessionModel).filter_by(user_id=req.context['user'].id).delete(
                synchronize_session=False)
            req.context['session'].commit()
        raise falcon.HTTPFound('/app/login')
