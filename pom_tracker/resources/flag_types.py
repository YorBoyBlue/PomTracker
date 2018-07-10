from models.flag_types_model import FlagTypeModel


class FlagTypesResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.content = req.context['session'].query(
            FlagTypeModel.flag_type).all()
