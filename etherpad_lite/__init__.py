from functools import partial
import json

import urllib3


def utf8_encode(s):
    return s if isinstance(s, bytes) else s.encode('utf8')


def utf8_encode_dict_values(d):
    return {k: utf8_encode(v) for k, v in d.items()}


class EtherpadException(Exception): pass


class EtherpadLiteClient(object):

    http = urllib3.PoolManager()

    def __init__(self, base_params={}, base_url='http://localhost:9001/api',
                       api_version='1', timeout=20):
        self.api_version = api_version
        self.base_params = utf8_encode_dict_values(base_params)
        self.base_url = base_url
        self.timeout = timeout

    def __call__(self, path, **params):
        params = utf8_encode_dict_values(params)
        data = dict(self.base_params, **params)
        url = '%s/%s/%s' % (self.base_url, self.api_version, path)
        r = self.http.request('POST', url, fields=data, timeout=self.timeout)
        r = json.loads(r.data.decode('utf-8'))
        if not r or not isinstance(r, dict):
            raise EtherpadException('API returned: %s' % r)
        if r.get('code') != 0:
            raise EtherpadException(r.get('message', r))
        return r.get('data')

    def __getattr__(self, name):
        return partial(self, name)
