from models.pomodoro_model import PomodoroModel


class PomodoroCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        pom_rows = req.context['session'].query(
            PomodoroModel).filter_by(user_id=req.context['user'].id).all()

        poms = []
        for row in pom_rows:
            pom = {
                'task': row.task,
                'review': row.review,
                'created': row.created.strftime('%Y-%m-%d'),
                'distractions': row.distractions,
                'pom_success': row.pom_success,
                'start_time': row.start_time.strftime('%I:%M%p').strip('0'),
                'end_time': row.end_time.strftime('%I:%M%p').strip('0')
            }
            poms.append(pom)

        resp.media = poms
