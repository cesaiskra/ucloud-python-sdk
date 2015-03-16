this is a python sdk for ucloud

usage:

from ucloud_python_sdk import client as uclient

cl=uclient(base_url, public_key, private_key)

#creat a UHostInstance
#result={retcode=0,id="abasdfdf"}
result=cl.Instance.create(region="cn-north-03",imageId="uimage-qiut5g",loginMode="Password",password="yanheventest",tag="Group1",type="BD")

