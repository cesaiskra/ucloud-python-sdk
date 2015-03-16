#-*- encoding: utf-8 -*-
import hashlib,json,httplib
import urlparse
import urllib
import requests

import utils
import exceptions

class HTTPClient(object):
    USER_AGENT = 'python-ucloudclient'


    def request(self, url, method, **kwargs):
            kwargs.setdefault('headers', kwargs.get('headers', {}))
            kwargs['headers']['User-Agent'] = self.USER_AGENT
            kwargs['headers']['Accept'] = 'application/json'
            if 'body' in kwargs:
                kwargs['headers']['Content-Type'] = 'application/json'
                kwargs['data'] = json.dumps(kwargs['body'])
                del kwargs['body']

            resp = requests.request(
                method,
                url,
                **kwargs)

            if resp.text:
                if resp.status_code == 400:
                    if ('Connection refused' in resp.text or
                            'actively refused' in resp.text):
                        raise exceptions.ConnectionRefused(resp.text)
                try:
                    body = json.loads(resp.text)
                except ValueError:
                    body = None
            else:
                body = None

            if resp.status_code >= 400:
                raise exceptions.from_response(resp, body, url, method)

            return resp, body

    def get(self, url, **kwargs):
        return self.request(url, 'GET', **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, 'POST', **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'DELETE', **kwargs)

