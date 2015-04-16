import logging
import argparse

from utils import shell_utils
from utils import api_utils


logger = logging.getLogger(__name__)


def _key_value_pairing(text):
    try:
        (k, v) = text.split('=', 1)
        return (k, v)
    except ValueError:
        msg = "%r is not in the format of key=value" % text
        raise argparse.ArgumentTypeError(msg)


def _print_result(d):
    for i in d:
        if 'Id' in i:
            print('ID:%s\nOperated Sucessfully!!'%d[i])
    return 0


def _print_host(d):
    # d={u'Remark': u'', u'Tag': u'Default', u'Name': u'yan-1',
    #     u'DiskSet': [{u'Type': u'Boot', u'Drive': u'/dev/sda',
    #     u'DiskId': u'ce3b1751-d837-4949-9c73-29368b7fe820',
    #     u'Size': 20}], u'IPSet': [{u'IP': u'10.11.1.126', u'Type': u'Private'},
    #     {u'IPId': u'eip-yci4qr', u'IP': u'107.150.97.103', u'Bandwidth': 2,
    #     u'Type': u'International'}], u'CPU': 1, u'State': u'Running',
    #     u'BasicImageId': u'uimage-nhwrqn', u'ImageId': u'ce3b1751-d837-4949-9c73-29368b7fe820',
    #     u'ExpireTime': 1429632272, u'UHostType': u'Normal', u'UHostId': u'uhost-4dmzop',
    #     u'NetworkState': u'Connected', u'ChargeType': u'Month', u'Memory': 2048,
    #     u'OsType': u'Linux', u'CreateTime': 1426953872, u'BasicImageName': u'Ubuntu 14.04 64\u4f4d'}
    # import pdb
    # pdb.set_trace()
    disk_set=d.pop('DiskSet')
    ip_set=d.pop('IPSet')
    if d.get('ExpireTime'):
        d['ExpireTime']= api_utils.get_formate_time(d['ExpireTime'])
    if d.get('CreateTime'):
        d['CreateTime']= api_utils.get_formate_time(d['CreateTime'])

    for i in range(len(disk_set)):
        disk=disk_set[i]
        exp_time=disk.get('ExpireTime')
        exp=''
        if exp_time:
            exp=" Exp:" + str(api_utils.get_formate_time(exp_time))
        disk_detail="%s %dGB Type:%s ID:%s %s"%(disk['Drive'],disk['Size'],disk['Type'],disk['DiskId'],exp)
        d['Disk_%d'%i]=disk_detail
    for j in range(len(ip_set)):
        ip=ip_set[j]
        bandwidth=''
        if ip.get('Bandwidth'):
            bandwidth=str(ip.get('Bandwidth',''))+"Mb/s"
        ip_id=''
        if ip.get('IPId'):
            ip_id="ID:"+str(ip.get('IPId'))
        ip_detail="%s %s %s %s"%(ip['Type'],bandwidth,ip['IP'],ip_id)
        d['IP_%d'%j]=ip_detail
    shell_utils.print_dict(d)


@shell_utils.arg(
    '--name',
    default=None,
    metavar='<name>',
    help=("Name or host."))
@shell_utils.arg(
    '--imageid',
    default=None,
    metavar='<imageid>',
    help=("imageid or host."))
@shell_utils.arg(
    '--loginmode',
    default=None,
    metavar='<loginmode>',
    help=("loginmode or host."))
@shell_utils.arg(
    '--loginmode',
    default=None,
    metavar='<loginmode>',
    help=("loginmode or host."))
@shell_utils.arg(
    '--password',
    default=None,
    metavar='<password>',
    help=("password or host."))
@shell_utils.arg(
    '--keypair',
    default=None,
    metavar='<keypair>',
    help=("keypair or host."))
@shell_utils.arg(
    '--cpu',
    default=None,
    type=int,
    metavar='<cpu>',
    help=("cpu or host."))
@shell_utils.arg(
    '--memory',
    default=None,
    type=int,
    metavar='<memory>',
    help=("memory or host."))
@shell_utils.arg(
    '--diskspace',
    default=None,
    type=int,
    metavar='<diskspace>',
    help=("diskspace or host."))
@shell_utils.arg(
    '--networkid',
    default=None,
    metavar='<networkid>',
    help=("networkid or host."))
@shell_utils.arg(
    '--securitygroupid',
    default=None,
    metavar='<securitygroupid>',
    help=("securitygroupid or host."))
@shell_utils.arg(
    '--chargetype',
    default=None,
    metavar='<chargetype>',
    help=("chargetype or host."))
@shell_utils.arg(
    '--quantity',
    default=None,
    metavar='<quantity>',
    help=("quantity or host."))
def do_uhost_create(cs,args):
    '''
    boot a host
    '''
    print args
    cs.uhost.create(args.ucloud_region,args.imageid,args.loginmode)
    return 0


@shell_utils.arg(
    '--uhostid',
    default=None,
    metavar='<uhostid>',
    help=("uhostid or host."))
def do_uhost_start(cs,args):
    '''
    start a host
    '''
    print args
    result=cs.uhost.start(args.ucloud_region,args.uhostid)
    _print_result(result)


@shell_utils.arg(
    '--uhostid',
    default=None,
    metavar='<uhostid>',
    help=("uhostid or host."))
def do_uhost_stop(cs,args):
    '''
    stop a host
    '''
    print args
    result=cs.uhost.stop(args.ucloud_region,args.uhostid)
    _print_result(result)


@shell_utils.arg(
    '--uhostid',
    default=None,
    metavar='<uhostid>',
    help=("uhostid or host."))
def do_uhost_delete(cs,args):
    '''
    terminate a host
    '''
    print args
    result=cs.uhost.terminate(args.ucloud_region,args.uhostid)
    _print_result(result)

@shell_utils.arg(
    '--uhostid',
    default=None,
    metavar='<uhostid>',
    help=("uhostid or host."))
def do_uhost_reboot(cs,args):
    '''
    reboot a host
    '''
    print args
    result=cs.uhost.reboot(args.ucloud_region,args.uhostid)
    _print_result(result)


@shell_utils.arg(
    '--uhostid',
    default=None,
    metavar='<uhostid>',
    help=("uhostid or host."))
def do_uhost_show(cs,args):
    '''
    show detail of a host
    '''
    print args
    host=cs.uhost.get(args.ucloud_region,[args.uhostid]).get('UHostSet')[0]
    _print_host(host)


def do_uhost_list(cs,args):
    '''
    list  uhosts
    '''
    uhosts = cs.uhost.get(args.ucloud_region).get('UHostSet')
    shell_utils.print_list(uhosts,['UHostId','Name','Tag','State','BasicImageName'])


def do_uhost_image_list(cs,args):
    '''
    list all images
    '''
    images=cs.uhost.get_image(args.ucloud_region).get('ImageSet')
    shell_utils.print_list(images,['ImageId','ImageName'])