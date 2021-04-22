import os
import falcon
from falcon import media
from wsgiref.simple_server import make_server

from .error_handling.error_handler import error_handler

from .middlewares.config_middleware import ConfigMiddleware
from .middlewares.validation_middleware import ValidationMiddleware
from .middlewares.negotiation_middleware import NegotiationMiddleware
from .middlewares.user_middleware import UserMiddleware

from .resources.user_logout import UserLogoutResource
from .resources.home import HomeResource
from .resources.user_create import UserCreateResource
from .resources.user_create_email_exists import UserCreateEmailExistsResource
from .resources.user_login import UserLoginResource
from .resources.user_login_failed import UserLoginFailedResource
from .resources.user_settings import UserSettingsResource
from .resources.pomodoro_collection_export import PomodoroCollectionExportResource
from .resources.pomodoro_delete import PomodoroDeleteResource
from .resources.user_session_expired import UserSessionExpiredResource
from .resources.pomodoro_today import PomodoroTodayResource
from .resources.pomodoro_collection import PomodoroCollectionResource
from .resources.pomodoro_today_export import PomodoroTodayExportResource


class Application:
    app: falcon.App

    def __init__(self):

        # handlers = media.Handlers({
        #     'application/json': media.JSONHandler(),
        #     'application/x-www-form-urlencoded': media.multipart.MultipartFormHandler()
        # })
        config_middleware = ConfigMiddleware()
        validation_middleware = ValidationMiddleware()
        negotiation_middleware = NegotiationMiddleware()
        user_middleware = UserMiddleware()

        self.app = falcon.App(middleware=[
            config_middleware, user_middleware, validation_middleware, negotiation_middleware
        ])
        # self.app.req_options.media_handlers = handlers
        self.app.req_options.auto_parse_form_urlencoded = True
        # self.app.resp_options.media_handlers = handlers
        self.app.add_error_handler(Exception, error_handler)
        self.app.resp_options.secure_cookies_by_default = False

        # Routes
        self.app.add_route('/home', HomeResource())
        self.app.add_route('/user/create', UserCreateResource())
        self.app.add_route('/user/create_email_exists', UserCreateEmailExistsResource())
        self.app.add_route('/user/login', UserLoginResource())
        self.app.add_route('/user/login_failed', UserLoginFailedResource())
        self.app.add_route('/user/logout', UserLogoutResource())
        self.app.add_route('/user/settings', UserSettingsResource())
        self.app.add_route('/user/session_expired', UserSessionExpiredResource())
        self.app.add_route('/pomodoro/today', PomodoroTodayResource())
        self.app.add_route('/pomodoro/today/export', PomodoroTodayExportResource())
        self.app.add_route('/pomodoro/collection', PomodoroCollectionResource())
        self.app.add_route('/pomodoro/collection/export', PomodoroCollectionExportResource())
        self.app.add_route('/pomodoro/delete', PomodoroDeleteResource())

        # Static routes
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.app.add_static_route('/css', dir_path + '/assets/css')
        self.app.add_static_route('/images', dir_path + '/assets/images')
        self.app.add_static_route('/js', dir_path + '/assets/js')

    def start_app(self, forever=False):
        httpd = make_server('localhost', 1987, self.app)

        if forever:
            httpd.serve_forever()
        else:
            httpd.handle_request()

    # def create_db(self):
    #     dbm.Base.metadata.create_all(dbm.engine)
