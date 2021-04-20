import falcon
import os
from falcon import media
from wsgiref.simple_server import make_server
from error_handling.error_handler import error_handler
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
from resources.pomodoro_collection_today import PomodoroCollectionTodayResource
from resources.pomodoro_collection import PomodoroCollectionResource
from resources.pom_validation import PomodoroValidationResource
from resources.flag_types import FlagTypesResource
from resources.pom_sheet_export import PomSheetExportResource
from models.base_model import BaseModel


class Application:
    app: falcon.App
    db_middleware: DatabaseMiddleware

    def __init__(self):

        handlers = media.Handlers({
            'application/json': media.JSONHandler()
        })
        self.db_middleware = DatabaseMiddleware()
        config_middleware = ConfigMiddleware()
        validation_middleware = ValidationMiddleware()
        negotiation_middleware = NegotiationMiddleware()
        user_middleware = UserMiddleware()

        self.app = falcon.App(middleware=[
            self.db_middleware, config_middleware, user_middleware,
            validation_middleware, negotiation_middleware
        ])
        self.app.req_options.media_handlers = handlers
        self.app.req_options.auto_parse_form_urlencoded = True
        self.app.resp_options.media_handlers = handlers
        self.app.add_error_handler(Exception, error_handler)
        self.app.resp_options.secure_cookies_by_default = False

        # Routes
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Home route
        self.app.add_route('/app/home', HomeResource())
        # User routes
        self.app.add_route('/app/create', UserCreateResource())
        self.app.add_route('/app/create_email_exists',
                           UserCreateEmailExistsResource())
        self.app.add_route('/app/login', UserLoginResource())
        self.app.add_route('/app/login_failed', UserLoginFailedResource())
        self.app.add_route('/app/session_expired', SessionExpiredResource())
        self.app.add_route('/app/logout', UserLogoutResource())
        self.app.add_route('/api/users', UserCollectionResource())
        # Session routes
        self.app.add_route('/api/session', SessionResource())
        # Pomodoro routes
        self.app.add_route('/app/pomodoro', PomodoroResource())
        self.app.add_route('/app/pomodoro_set', PomodoroSetResource())
        self.app.add_route('/app/pom_exists', PomodoroExistsErrorResource())
        self.app.add_route('/app/pom_invalid',
                           PomodoroValidationErrorResource())
        self.app.add_route('/api/pom_validation', PomodoroValidationResource())
        self.app.add_route('/api/poms/today',
                           PomodoroCollectionTodayResource())
        self.app.add_route('/api/poms', PomodoroCollectionResource())
        self.app.add_route('/api/delete_poms', DeletePomsResource())
        self.app.add_route('/api/flag_types', FlagTypesResource())
        self.app.add_route('/api/pom_sheet_export', PomSheetExportResource())
        self.app.add_route('/app/export_poms', ExportPomsResource())
        # Settings route
        self.app.add_route('/app/settings', UserSettingsResource())
        # Static directory routes
        self.app.add_static_route('/css', dir_path + '/css')
        self.app.add_static_route('/js', dir_path + '/js')
        self.app.add_static_route('/assets', dir_path + '/assets')

    def start_app(self, forever=False):
        httpd = make_server('localhost', 1987, self.app)

        if forever:
            httpd.serve_forever()
        else:
            httpd.handle_request()

    # def create_db(self):
    #     BaseModel.metadata.create_all(self.db_middleware.engine)
