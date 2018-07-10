from models.pom_flags_model import PomFlagsModel


class PomFlagsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        # resp.content = req.context['session'].query(
        #     FlagTypeModel.flag_type).all()
