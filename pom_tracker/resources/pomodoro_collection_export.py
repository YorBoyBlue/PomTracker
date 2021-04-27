from resources.resourse_base import ResourceBase
from mako.template import Template
import json
from controllers.pomodoro import export_collection


class PomodoroCollectionExportResource(ResourceBase):
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/pomodoro_export_view.mako')
        resp.text = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        post = req.get_media()
        user_id = req.context['user'].id

        # Parse POST variables
        start_date = self.get_param(post.get('start_date'))
        end_date = self.get_param(post.get('end_date'))

        data = export_collection(user_id, start_date, end_date)

        filename = str(start_date) + '_to_' + str(end_date) + '_Arin_Poms.json'
        resp.text = json.dumps(data, indent=2)
        resp.downloadable_as = filename
        resp.content_type = 'application/octet-stream'
