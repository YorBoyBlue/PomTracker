from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseMiddleware:
    def __init__(self):
        self.engine = create_engine('sqlite:///database/pom_tracker.db')

        self.Session = sessionmaker(bind=self.engine)

    def process_request(self, req, resp):
        req.context['session'] = self.Session()
