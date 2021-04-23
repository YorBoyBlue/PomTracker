class ResourceBase:
    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        pass

    def get_param(self, value, default=None):
        if not value:
            return default
        elif isinstance(value, str):
            return value
        else:
            return default

    def get_param_as_list(self, value, default=None):
        if not value:
            return default
        elif isinstance(value, list):
            return value
        elif isinstance(value, str):
            return [value]
        else:
            return default
