from falcon.media import BaseHandler
from falcon import errors
from urllib.parse import parse_qs, parse_qsl


class URLEncodedHandler(BaseHandler):
    def deserialize(self, raw):
        try:
            if not raw:
                return {}
            else:
                qs = parse_qs(raw)
                # qs = {k: [v, v, ...], k: [v]}
                # I don't care what is in the dict just that I return a dict
                return {k.decode('utf-8'): v.pop().decode('utf-8')
                        for k, v in qs.items()}

                # qsl = parse_qsl(raw)
                # # qsl = [(k, v), (k, v), ...]
                # return {t[0]: t[1] for t in qsl}
        except ValueError as err:
            raise errors.HTTPBadRequest(
                'Invalid urlencoded',
                'Could not parse urlencoded body - {0}'.format(err)
            )

    def serialize(self, media):
        return media.encode('utf-8')