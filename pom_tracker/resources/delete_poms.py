import falcon
from models.pomodoro_model import PomodoroModel
from models.pom_flags_model import PomFlagsModel
from database.database_manager import dbm


class DeletePomsResource:
    def on_post(self, req, resp):
        """Handles POST requests"""

        db = dbm.get_db()

        poms_to_delete_ids = req.get_param_as_list('poms_to_delete')

        db.query(PomodoroModel).filter(PomodoroModel.id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        db.query(PomFlagsModel).filter(PomFlagsModel.pom_id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        db.commit()

        raise falcon.HTTPFound('/pomodoro')
