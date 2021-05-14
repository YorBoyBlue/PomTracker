import falcon
from ..resources.resourse_base import ResourceBase
from ..controllers.pomodoro import delete


class PomodoroDeleteResource(ResourceBase):
    def on_post(self, req, resp):
        """Handles POST requests"""

        post = req.get_media()

        # Parse POST variables to be submitted to DB
        poms_to_delete_ids = self.get_param_as_list(post.get('poms_to_delete'))
        delete(poms_to_delete_ids)

        raise falcon.HTTPFound('/pomodoro/today')
