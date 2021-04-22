from mako.template import Template
import json
from controllers.pomodoro import export_collection


class PomodoroCollectionExportResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/pomodoro_export_view.mako')
        resp.text = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        user_id = req.context['user'].id
        start_date = req.get_param('start_date')
        end_date = req.get_param('end_date')

        data = export_collection(user_id, start_date, end_date)

        filename = str(start_date) + '-' + str(
            end_date) + '_Arin_Pom_Sheets.json'
        resp.text = json.dumps(data, indent=2)
        resp.downloadable_as = filename
        resp.content_type = 'application/octet-stream'
