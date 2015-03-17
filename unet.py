import base

class UnetManager(base.Manager):
    '''
    net manager class
    '''
    def sec_get(self,region,resourcetype=None,resourceid=None,groupid=None):
        body={}
        body['Region']=region
        body['Action']='DescribeSecurityGroup'
        if resourcetype:
            body['ResourceType']=resourcetype
        if resourceid:
            body['ResourceId']=resourceid
        if groupid:
            body['GroupId']=groupid
        return self._get(body)

    def eip_get(self,region,eipids=None,offset=None,limit=None):
        '''
        query host in given region or given host id
        :param region:
        :param uhostids:
        :param offset:
        :param limit:
        :return:
        '''
        body={}
        body['Region']=region
        body['Action']="DescribeEIP"
        if eipids:
            for i in range(len(eipids)):
                body['UHostIds.'+str(i)]=eipids[i]
        return self._get(body)