import falcon
import os
from falcon import media
from wsgiref.simple_server import make_server
from error_handling.error_handler import error_handler
from handlers.handler_urlencoded import URLEncodedHandler
from middlewares.config_middleware import ConfigMiddleware
from middlewares.db_middleware import DatabaseMiddleware
from middlewares.validation_middleware import ValidationMiddleware
from middlewares.negotiation_middleware import NegotiationMiddleware
from middlewares.user_middleware import UserMiddleware
from resources.user_logout import UserLogoutResource
from resources.user_collection import UserCollectionResource
from views.home import HomeResource
from views.user_create import UserCreateResource
from views.user_create_email_exists import UserCreateEmailExistsResource
from views.user_login import UserLoginResource
from views.user_login_failed import UserLoginFailedResource
from views.user_settings import UserSettingsResource
from views.export_poms import ExportPomsResource
from views.pomodoro_set import PomodoroSetResource
from resources.delete_poms import DeletePomsResource
from resources.session import SessionResource
from views.session_expired import SessionExpiredResource
from views.pomodoro import PomodoroResource
from views.partials.pomodoro_exists_error import PomodoroExistsErrorResource
from views.partials.pomodoro_validation_error import \
    PomodoroValidationErrorResource
from resources.pomodoro_collection import PomodoroCollectionTodayResource
from resources.pomodoro_collection_all import PomodoroCollectionResource
from resources.pom_validation import PomodoroValidationResource
from resources.pomodoro_replace import PomodoroReplaceResource
from resources.flag_types import FlagTypesResource
from resources.pom_sheet_export import PomSheetExportResource
from models.base_model import BaseModel


class Application:

    def __init__(self):
        handlers = media.Handlers({
            'application/json': media.JSONHandler(),
            'application/x-www-form-urlencoded': URLEncodedHandler()
        })
        self.db_middleware = DatabaseMiddleware()
        self.config_middleware = ConfigMiddleware()
        self.validation_middleware = ValidationMiddleware()
        self.negotiation_middleware = NegotiationMiddleware()
        self.user_middleware = UserMiddleware()

        self.api = falcon.API(middleware=[
            self.config_middleware, self.db_middleware, self.user_middleware,
            self.validation_middleware, self.negotiation_middleware
        ])
        self.api.req_options.media_handlers = handlers
        self.api.resp_options.media_handlers = handlers
        self.api.add_error_handler(Exception, error_handler)
        self.api.resp_options.secure_cookies_by_default = False

        # Routes
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Home route
        self.api.add_route('/app/home', HomeResource())
        # User routes
        self.api.add_route('/app/create', UserCreateResource())
        self.api.add_route('/app/create_email_exists',
                           UserCreateEmailExistsResource())
        self.api.add_route('/app/login', UserLoginResource())
        self.api.add_route('/app/login_failed', UserLoginFailedResource())
        self.api.add_route('/app/session_expired', SessionExpiredResource())
        self.api.add_route('/app/logout', UserLogoutResource())
        self.api.add_route('/api/users', UserCollectionResource())
        # Session routes
        self.api.add_route('/api/session', SessionResource())
        # Pomodoro routes
        self.api.add_route('/app/pomodoro', PomodoroResource())
        self.api.add_route('/app/pomodoro_set', PomodoroSetResource())
        self.api.add_route('/app/pom_exists', PomodoroExistsErrorResource())
        self.api.add_route('/app/pom_invalid',
                           PomodoroValidationErrorResource())
        self.api.add_route('/api/pom_validation', PomodoroValidationResource())
        self.api.add_route('/api/poms/today',
                           PomodoroCollectionTodayResource())
        self.api.add_route('/api/poms', PomodoroCollectionResource())
        self.api.add_route('/api/pom_replace', PomodoroReplaceResource())
        self.api.add_route('/api/delete_poms', DeletePomsResource())
        self.api.add_route('/api/flag_types', FlagTypesResource())
        self.api.add_route('/api/pom_sheet_export', PomSheetExportResource())
        self.api.add_route('/app/export_poms', ExportPomsResource())
        # Settings route
        self.api.add_route('/app/settings', UserSettingsResource())
        # Static directory routes
        self.api.add_static_route('/css', dir_path + '/css')
        self.api.add_static_route('/js', dir_path + '/js')
        self.api.add_static_route('/assets', dir_path + '/assets')

    def start_app(self, forever=False):
        httpd = make_server('localhost', 8000, self.api)

        if forever:
            httpd.serve_forever()
        else:
            httpd.handle_request()

    def create_db(self):
        BaseModel.metadata.create_all(self.db_middleware.engine)


# Entry point for the application
if __name__ == '__main__':
    app = Application()
    app.start_app(forever=True)
    # app.start_app()
