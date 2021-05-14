import falcon
import datetime
import re
from sqlalchemy.sql import select
from sqlalchemy.orm.exc import NoResultFound
from ..models.session_model import session_table
from ..database.database_manager import dbm


class AuthMiddleware:

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

                cookies = req.cookies
                if 'pomodoro_login_hash' in cookies:
                    my_cookie_hash = cookies.get('pomodoro_login_hash', None)
                    if my_cookie_hash is not None:
                        with dbm() as conn:
                            try:
                                query = select(session_table).where(
                                    session_table.c.hash == my_cookie_hash)
                                result = conn.execute(query)
                                user_session = result.fetchone()

                            except NoResultFound:
                                resp.unset_cookie('pomodoro_login_hash')
                                raise falcon.HTTPFound('/user/login')

                            else:
                                session_modified_time = user_session.modified
                                tdelta = datetime.timedelta(hours=22)
                                now = datetime.datetime.utcnow()
                                session_expire_time = session_modified_time + tdelta

                                if now > session_expire_time:
                                    query = session_table.delete().where(
                                        session_table.c.user_id == req.context['user'].id)
                                    conn.execute(query)
                                    raise falcon.HTTPFound('/user/session_expired')

                else:
                    raise falcon.HTTPFound('/user/login')
