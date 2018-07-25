import falcon
from models.user_model import UserModel
from models.session_model import SessionModel
from sqlalchemy.orm.exc import NoResultFound
import re


class UserMiddleware:

    def process_request(self, req, resp):
        valid_uri_pattern = '/app/pomodora'
        pattern = re.compile(valid_uri_pattern)
        is_valid = False
        if pattern.match(valid_uri_pattern) is not None:
            pass
            # is_valid = True

        if req.path in req.context['included_paths_user']:
            my_cookie_hash = req.cookies.get('pomodora_login_hash', None)
            if my_cookie_hash is not None:
                try:
                    user_session = req.context['session'].query(
                        SessionModel, SessionModel.user_id).filter_by(
                        hash=my_cookie_hash).one()

                except NoResultFound as e:
                    # User session was not found, send user to session
                    # expired login
                    raise falcon.HTTPFound('/app/session_expired')

                else:
                    # User session was found, try to query user
                    try:
                        user = req.context['session'].query(
                            UserModel).filter_by(id=user_session.user_id).one()
                        a = ''

                    except NoResultFound as e:
                        # User was not found, send user to session
                        # expired login
                        raise falcon.HTTPFound('/app/session_expired')

                    else:
                        # User was found, pass it through the request context
                        req.context['user'] = user
