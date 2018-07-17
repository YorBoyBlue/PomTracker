import falcon
from models.pomodora_model import PomodoraModel
from models.pom_flags_model import PomFlagsModel


class DeletePomsResource:
    def on_post(self, req, resp):
        """Handles POST requests"""

        poms_to_delete_ids = req.media['poms_to_delete']

        req.context['session'].query(PomodoraModel).filter(
            PomodoraModel.id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        req.context['session'].query(PomFlagsModel).filter(
            PomFlagsModel.pom_id.in_(poms_to_delete_ids)).delete(
            synchronize_session=False)
        req.context['session'].commit()

        raise falcon.HTTPFound('/app/pomodora')
