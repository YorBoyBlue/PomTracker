import falcon
from models.pomodoro_model import PomodoroModel
from models.pom_flags_model import PomFlagsModel


class DeletePomsResource:
    def on_post(self, req, resp):
        """Handles POST requests"""

        poms_to_delete_ids = req.get_param_as_list('poms_to_delete')

        req.context['session'].query(PomodoroModel).filter(
            PomodoroModel.id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        req.context['session'].query(PomFlagsModel).filter(
            PomFlagsModel.pom_id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        req.context['session'].commit()

        raise falcon.HTTPFound('/app/pomodoro')
