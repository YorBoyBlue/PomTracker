import json
from helpers.my_requests import Requests
from resources.pomodora_collection import PomodoraCollectionResource
from datetime import datetime, date


class PomSheetExport:
    def on_get(self, req, resp):
        todays_poms = Requests().get(req, resp, PomodoraCollectionResource())
        data = {'poms': []}
        for row in todays_poms:
            pom = {
                'add_date': datetime.strftime(row.add_date, '%Y-%m-%d'),
                'title': row.task,
                'start_time': row.start_time.strftime('%I:%M%p'),
                'end_time': row.end_time.strftime('%I:%M%p'),
                'review': row.review,
                'flags': []
            }
            for flag in row.flags:
                pom['flags'].append(flag.flag_type)
            data['poms'].append(pom)

        today = date.today()
        filename = str(today) + '-Arin_Pom_Sheet.json'
        with open('pom_sheets/' + filename, 'w') as outfile:
            json.dump(data, outfile, indent=2)
