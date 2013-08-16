import httplib, urllib

field_keys = ['field' + str(n) for n in xrange(1,9)]
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}


class channel(object):
    def __init__(self, key):
        self.key = key

    def update(self, *vals):
        params = urllib.urlencode(zip(field_keys, vals) + [('key', self.key)])
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        conn.close()
        return response
