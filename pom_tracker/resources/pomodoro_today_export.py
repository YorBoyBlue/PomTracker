import json
from ..controllers.pomodoro import export_today
from datetime import date


class PomodoroTodayExportResource:
    def on_get(self, req, resp):
        user_id = req.context['user'].id
        data = export_today(user_id)

        today = date.today()
        filename = str(today) + '-Arin_Pom_Sheet.json'
        resp.text = json.dumps(data, indent=2)
        resp.downloadable_as = filename
        resp.content_type = 'application/octet-stream'
