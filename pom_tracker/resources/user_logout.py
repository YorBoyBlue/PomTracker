import falcon
from models.session_model import SessionModel
from database.database_manager import dbm


class UserLogoutResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        db = dbm.get_db()

        cookies = req.cookies
        if 'pomodoro_login_hash' in cookies:
            # This will remove the cookie because we are overriding the existing one with a
            # negative max_age
            resp.set_cookie('pomodoro_login_hash', '', max_age=-1, path='/')
            db.query(SessionModel).filter_by(user_id=req.context['user'].id).delete(
                synchronize_session=False)
            db.commit()
        raise falcon.HTTPFound('/user/login')
