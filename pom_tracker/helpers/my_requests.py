class Requests:
    @staticmethod
    def get(req, resp, resource):
        resource.on_get(req, resp)
        return resp.content

    @staticmethod
    def validate_get(req, resp, resource):
        resource.on_get(req, resp)
