import falcon
import datetime
from sqlalchemy.orm.exc import NoResultFound
from models.session_model import SessionModel


class SessionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        cookies = req.cookies
        if 'pomodora_login_hash' in cookies:
            my_cookie_hash = cookies.get('pomodora_login_hash', None)
            if my_cookie_hash is not None:
                try:
                    my_session = req.context['session'].query(
                        SessionModel, SessionModel.hash,
                        SessionModel.modified). \
                        filter_by(hash=my_cookie_hash).one()

                except NoResultFound:
                    resp.unset_cookie('pomodora_login_hash')
                    raise falcon.HTTPFound('/app/login')

                else:
                    session_modified_time = my_session.modified
                    tdelta = datetime.timedelta(hours=2)
                    now = datetime.datetime.utcnow()
                    session_expire_time = session_modified_time + tdelta

                    if now > session_expire_time:
                        raise falcon.HTTPFound('/app/session_expired')

        else:
            raise falcon.HTTPFound('/app/login')
