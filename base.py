#-*- encoding: utf-8 -*-
import json,httplib
import urlparse
import urllib

import utils
import uexceptions

class HTTPClient(object):

    def __init__(self, base_url):
        self.base_url = base_url
        o = urlparse.urlsplit(base_url)
        if o.scheme == 'https':
            self.conn = httplib.HTTPSConnection(o.netloc);
        else:
            self.conn = httplib.HTTPConnection(o.netloc);

    def __del__(self):
        self.conn.close()


    def get(self, resouse, params):
        resouse += "?" + urllib.urlencode(params)
        print("%s%s" % (self.base_url, resouse))
        response=None

        try:
            self.conn.request("GET", resouse)

        except Exception as e:
            raise uexceptions.ConnectionRefused(e)

        respones_raw=self.conn.getresponse().read()

        try:
            response = json.loads(respones_raw)

        except Exception as e:
            raise uexceptions.NoJsonFound(e)

        if response.get('RetCode')!=0:
            raise uexceptions.BadParameters('bad parameters:%s'%params)
        return response


class Manager(object):
    def __init__(self,api):
        self.api=api

    def _get(self, body):
        body['PublicKey']=self.api.public_key
        token=utils.get_token(self.api.private_key,body)
        body['Signature']=token
        return self.api.client.get('/',body)


class APIResourceWrapper(object):
    """ wrapper for api objects. """
    _attrs = []
    _apiresource = None

    def __init__(self, apiresource):
        self._apiresource = apiresource

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if attr not in self._attrs:
                raise
            # __getattr__ won't find properties
            return getattr(self._apiresource, attr)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             dict((attr, getattr(self, attr))
                                  for attr in self._attrs
                                  if hasattr(self, attr)))

