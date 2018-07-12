import falcon
import datetime
from sqlalchemy.orm.exc import NoResultFound
from models.session_model import SessionModel


class SessionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        cookies = req.cookies
        if 'my_hash' in cookies:
            my_cookie_hash = cookies.get('my_hash', None)
            if my_cookie_hash is not None:
                try:
                    my_session = req.context['session'].query(
                        SessionModel, SessionModel.hash,
                        SessionModel.create_date). \
                        filter_by(hash=my_cookie_hash).one()

                except NoResultFound:
                    resp.unset_cookie('my_hash')
                    raise falcon.HTTPFound('/app/login')

                else:
                    session_create_time = my_session.create_date
                    tdelta = datetime.timedelta(hours=2)
                    now = datetime.datetime.utcnow()
                    session_expire_time = session_create_time + tdelta

                    if now > session_expire_time:
                        resp.unset_cookie('my_hash')
                        raise falcon.HTTPFound('/app/login')

        else:
            raise falcon.HTTPFound('/app/login')
