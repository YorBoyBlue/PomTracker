import falcon
import datetime
import re
from sqlalchemy.orm.exc import NoResultFound
from models.session_model import SessionModel
from database.database_manager import dbm


class ValidationMiddleware:

    def process_request(self, req, resp):
        req_uri = req.path
        match_folder = False

        # Is the requests URI in an ignored folder
        for path in req.context['excluded_folders_validate']:
            pattern = re.compile(path)
            if pattern.match(req_uri) is not None:
                match_folder = True

        # Is the requests URI a specific ignored path
        if not match_folder:
            if req_uri not in req.context['excluded_paths_validate']:
                # Check if session exists and is not expired

                db = dbm.get_db()

                cookies = req.cookies
                if 'pomodoro_login_hash' in cookies:
                    my_cookie_hash = cookies.get('pomodoro_login_hash', None)
                    if my_cookie_hash is not None:
                        try:
                            my_session = db.query(
                                SessionModel.hash, SessionModel.modified).filter_by(
                                hash=my_cookie_hash).one()

                        except NoResultFound:
                            resp.unset_cookie('pomodoro_login_hash')
                            raise falcon.HTTPFound('/user/login')

                        else:
                            session_modified_time = my_session.modified
                            tdelta = datetime.timedelta(hours=22)
                            now = datetime.datetime.utcnow()
                            session_expire_time = session_modified_time + tdelta

                            if now > session_expire_time:
                                db.query(
                                    SessionModel).filter_by(user_id=req.context['user'].id).delete(
                                    synchronize_session=False)
                                db.commit()
                                raise falcon.HTTPFound('/user/session_expired')

                else:
                    raise falcon.HTTPFound('/user/login')
