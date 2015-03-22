#-*- encoding: utf-8 -*-
import json,httplib
import urlparse
import urllib

import api_utils
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
            print(response)

        except Exception as e:
            raise uexceptions.NoJsonFound(e)

        if response.get('RetCode')!=0:
            print('Message:%(Message)s\nRetCode:%(RetCode)s'%response)
            raise uexceptions.BadParameters("message: %s /n bad parameters:%s"%(response.get('Message'),params))
        return response


class Manager(object):
    def __init__(self,api):
        self.api=api

    def _get(self, body):
        body['PublicKey']=self.api.public_key
        token=api_utils.get_token(self.api.private_key,body)
        body['Signature']=token
        return self.api.client.get('/',body)