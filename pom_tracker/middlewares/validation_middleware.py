from helpers.my_requests import Requests
from resources.session import SessionResource
import re


class ValidationMiddleware:

    def process_request(self, req, resp):
        req_uri = req.path
        match_folder = False

        # Is the requests URI in an ignored folder
        for path in req.context['excluded_folders_validate']:
            pattern = re.compile(path)
            if pattern.match(req_uri) is not None:
                match_folder = True

        # Is the requests URI a specific ignored path
        if not match_folder:
            if req_uri not in req.context['excluded_paths_validate']:
                # Check if session exists and is not expired
                # Simulated downstream request
                Requests().get(req, resp, SessionResource())
