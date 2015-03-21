import logging
import argparse


logger = logging.getLogger(__name__)


def _key_value_pairing(text):
    try:
        (k, v) = text.split('=', 1)
        return (k, v)
    except ValueError:
        msg = "%r is not in the format of key=value" % text
        raise argparse.ArgumentTypeError(msg)


def do_uhost_create(cs,args):
    '''
    create a uhost
    :param cs:client
    :param args:
    :return:
    '''
    uhost = cs.uhost.create(args)