from helpers.my_requests import Requests
from resources.session import SessionResource


class ValidationMiddleware:
    def __init__(self):
        self.session_expire_time = 7200  # 2 hours in seconds

    def process_request(self, req, resp):
        # Check if session exists and is not expired
        # Simulated downstream request
        if req.relative_uri not in req.context['excluded_paths']:
            Requests().validate_get(req, resp, SessionResource())
