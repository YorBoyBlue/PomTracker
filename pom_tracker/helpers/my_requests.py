class Requests:
    @staticmethod
    def get(req, resp, resource):
        resource.on_get(req, resp)
