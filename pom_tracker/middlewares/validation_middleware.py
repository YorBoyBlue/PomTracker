from helpers.my_requests import Requests
from resources.session import SessionResource
import re


class ValidationMiddleware:
    def __init__(self):
        self.session_expire_time = 7200  # 2 hours in seconds

    def process_request(self, req, resp):
        req_uri = req.relative_uri
        match_folder = False
        for path in req.context['excluded_folders_validate']:
            pattern = re.compile(path)
            if pattern.match(req_uri) is not None:
                match_folder = True

        if not match_folder:
            if req_uri not in req.context['excluded_paths_validate']:
                # Check if session exists and is not expired
                # Simulated downstream request
                Requests().get(req, resp, SessionResource())
