this is a python sdk for ucloud,as well as a CLI tools for ucloud in linux bash
env.

usage:


	from ucloud-python-sdk import client as uclient    
	cl=uclient(base_url, public_key, private_key)    
    result=cl.uhost.create(region="cnnorth-03",imageId="uimageqiut5g",loginMode="Password",
						password="yanheventest",tag="Group1",type="BD")

