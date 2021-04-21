import json
from mako.template import Template
from models.pomodoro_model import PomodoroModel
from datetime import datetime
from database.database_manager import dbm


class ExportPomsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        resp.content_type = 'text/html'

        user_login_template = Template(filename='pom_tracker/views/export_poms_view.mako')
        resp.body = user_login_template.render()

    def on_post(self, req, resp):
        """Handles POST requests"""

        db = dbm.get_db()

        start_date = req.get_param('start_date')
        end_date = req.get_param('end_date')

        # Query poms within start and end dates
        poms = db.query(
            PomodoroModel).filter(PomodoroModel.created <= end_date). \
            filter(PomodoroModel.created >= start_date).filter_by(
            user_id=req.context['user'].id).order_by(
            PomodoroModel.created, PomodoroModel.start_time).all()

        data = {'poms': []}
        for row in poms:
            pom = {
                'created': datetime.strftime(row.created, '%Y-%m-%d'),
                'title': row.task,
                'start_time': row.start_time.strftime('%I:%M%p'),
                'end_time': row.end_time.strftime('%I:%M%p'),
                'distractions': row.distractions,
                'pom_success': row.pom_success,
                'review': row.review,
                'flags': []
            }
            for flag in row.flags:
                pom['flags'].append(flag.flag_type)
            data['poms'].append(pom)

        filename = str(start_date) + '-' + str(
            end_date) + '_Arin_Pom_Sheets.json'
        resp.body = json.dumps(data, indent=2)
        resp.downloadable_as = filename
        resp.content_type = 'application/octet-stream'
