from falcon.media import BaseHandler
from falcon import errors
from urllib.parse import parse_qs


class URLEncodedHandler(BaseHandler):
    def deserialize(self, raw):
        try:
            if not raw:
                return {}
            else:
                data = {}
                qs = parse_qs(raw)
                # I don't care what is in the dict just that I return a dict
                for k, v in qs.items():

                    # Create list element in the dict if necessary
                    if len(v) > 1:
                        data[k.decode('utf-8')] = []
                        for item in v:
                            data[k.decode('utf-8')].append(
                                item.decode('utf-8'))
                    # Just add the element to the dict
                    else:
                        if k.decode('utf-8') == 'flags' or k.decode(
                                'utf-8') == 'distractions' or k.decode(
                                'utf-8') == 'poms_to_delete':
                            data[k.decode('utf-8')] = []
                            data[k.decode('utf-8')].append(
                                v.pop().decode('utf-8'))

                        else:
                            data[k.decode('utf-8')] = v.pop().decode('utf-8')

                return data

        except ValueError as err:
            raise errors.HTTPBadRequest(
                'Invalid urlencoded',
                'Could not parse urlencoded body - {0}'.format(err)
            )

    def serialize(self, media):
        return media.encode('utf-8')
