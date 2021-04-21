from models.pomodoro_model import PomodoroModel
from database.database_manager import dbm


class PomodoroCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        db = dbm.get_db()

        limit = 20
        offset = req.get_param_as_int('offset', default=0)
        date_filter = req.get_param_as_date('date_filter')
        distractions_filter = req.get_param_as_int('distractions_filter')
        unsuccessful_filter = req.get_param_as_int('unsuccessful_filter')

        query = db.query(PomodoroModel).filter_by(user_id=req.context['user'].id)

        # Apply filters
        if date_filter:
            query = query.filter_by(created=date_filter)
        if distractions_filter:
            query = query.filter(PomodoroModel.distractions > 0)
        if unsuccessful_filter:
            query = query.filter_by(pom_success=0)

        # Get total count
        total_count = query.count()

        # Apply limit and offset
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)

        pom_rows = query.all()

        # Parse flags
        poms = []
        for row in pom_rows:
            flags = []
            for flag in row.flags:
                flags.append(flag.flag_type)
            pom = {
                'task': row.task,
                'review': row.review,
                'created': row.created.strftime('%Y-%m-%d'),
                'distractions': row.distractions,
                'flags': flags,
                'pom_success': row.pom_success,
                'start_time': row.start_time.strftime('%I:%M%p').strip('0'),
                'end_time': row.end_time.strftime('%I:%M%p').strip('0')
            }
            poms.append(pom)

        data = {
            'poms': poms,
            'total_count': total_count
        }

        resp.media = data
