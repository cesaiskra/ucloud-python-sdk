'''
ucloud python sdk client.
'''
import utils


class Client(object):
    '''
    ucloud python sdk client.
    '''
    def __init__(self,base_url,public_key,private_key):
        self.base_url=base_url
        self.private_key=private_key
        self.public_key=public_key


