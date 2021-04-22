import falcon
from controllers.pomodoro import delete


class PomodoroDeleteResource:
    def on_post(self, req, resp):
        """Handles POST requests"""

        poms_to_delete_ids = req.get_param_as_list('poms_to_delete')
        delete(poms_to_delete_ids)

        raise falcon.HTTPFound('/pomodoro/today')
