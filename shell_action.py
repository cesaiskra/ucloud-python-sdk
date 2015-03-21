import logging
import argparse

import shell_utils


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
    boot a host
    '''
    uhost = cs.uhost.create(args)


def do_uhost_list(cs,args):
    '''
    list  uhosts
    '''
    uhosts = cs.uhost.get(args.ucloud_region)
    shell_utils.print_list()


def do_uhost_show(cs,args):
    '''
    show a  uhost
    '''
    uhosts = cs.uhost.get(args.ucloud_region,args.id)


def do_uhost_image_list(cs,args):
    '''
    list all images
    '''
    images=cs.uhost.get_image(args.ucloud_region).get('ImageSet')
    shell_utils.print_list(images,['ImageId','ImageName'])