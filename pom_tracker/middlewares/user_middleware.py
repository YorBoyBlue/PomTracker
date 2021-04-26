import falcon
from sqlalchemy.sql import select
from sqlalchemy.orm.exc import NoResultFound
from models.user_model import user_table
from models.session_model import session_table
from database.database_manager import dbm


class UserMiddleware:

    def process_request(self, req, resp):

        if req.path in req.context['included_paths_user']:
            my_cookie_hash = req.cookies.get('pomodoro_login_hash', None)
            if my_cookie_hash is not None:

                with dbm() as conn:
                    try:
                        query = select(session_table).where(session_table.c.hash == my_cookie_hash)
                        result = conn.execute(query)
                        user_session = result.fetchone()

                    except NoResultFound as e:
                        # User session was not found, send user to session expired login
                        raise falcon.HTTPFound('/user/session_expired')

                    else:
                        # User session was found, try to query user
                        try:
                            query = select(user_table).where(user_table.c.id == user_session.user_id)
                            result = conn.execute(query)
                            user = result.fetchone()

                        except NoResultFound as e:
                            # User was not found, send user to session expired login
                            raise falcon.HTTPFound('/user/session_expired')

                        else:
                            # User was found, pass it through the request context
                            req.context['user'] = user
