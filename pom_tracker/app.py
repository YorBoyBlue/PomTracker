import falcon
import os
from falcon import media
from wsgiref.simple_server import make_server
from helpers.error_handler import error_handler
from handlers.handler_urlencoded import URLEncodedHandler
from middlewares.config_middleware import ConfigMiddleware
from middlewares.db_middleware import DatabaseMiddleware
from views.pomodora import PomodoraResource
from resources.pomodora_collection import PomodoraCollectionResource
from resources.flag_types import FlagTypesResource
from resources.pom_flags import PomFlagsResource
from resources.pom_sheet_export import PomSheetExport
from models.base_model import BaseModel


class Application:

    def __init__(self):
        handlers = media.Handlers({
            # falcon.MEDIA_MSGPACK: media.MessagePackHandler(),
            # falcon.MEDIA_JSON: media.JSONHandler(),
            'application/x-www-form-urlencoded': URLEncodedHandler()
        })
        self.db_middleware = DatabaseMiddleware()
        self.config_middleware = ConfigMiddleware()
        self.api = falcon.API(
            middleware=[self.db_middleware, self.config_middleware])
        self.api.req_options.media_handlers = handlers
        self.api.resp_options.media_handlers = handlers
        self.api.add_error_handler(Exception, error_handler)

        # routes
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.api.add_route('/app/pomodora', PomodoraResource())
        self.api.add_route('/app/reports?type=code', PomodoraResource())
        self.api.add_route('/api/poms', PomodoraCollectionResource())
        self.api.add_route('/api/flag_types', FlagTypesResource())
        self.api.add_route('/api/pom_flags', PomFlagsResource())
        self.api.add_route('/api/pom_sheet_export', PomSheetExport())
        self.api.add_static_route('/css', dir_path + '/css')

    def start_app(self, forever=False):
        httpd = make_server('localhost', 8000, self.api)

        if forever:
            httpd.serve_forever()
        else:
            httpd.handle_request()

    def create_db(self):
        BaseModel.metadata.create_all(self.db_middleware.engine)


if __name__ == '__main__':
    app = Application()
    app.start_app(forever=True)
    # app.start_app()
