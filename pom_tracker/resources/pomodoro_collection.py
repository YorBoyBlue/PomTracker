from mako.template import Template
from controllers.pomodoro import get_collection


class PomodoroCollectionResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        if req.content_type == 'application/json':
            # Return pomodoro collection

            limit = 20
            offset = req.get_param_as_int('offset', default=0)
            date_filter = req.get_param_as_date('date_filter')
            distractions_filter = req.get_param_as_int('distractions_filter')
            unsuccessful_filter = req.get_param_as_int('unsuccessful_filter')
            user_id = req.context['user'].id

            data = get_collection(
                user_id,
                limit,
                offset,
                date_filter,
                distractions_filter,
                unsuccessful_filter
            )

            resp.media = data
        else:
            # Load pomodoro collection endpoint
            resp.content_type = 'text/html'
            pomodoro_template = Template(
                filename='pom_tracker/views/pomodoro_collection_view.mako')
            resp.text = pomodoro_template.render()
