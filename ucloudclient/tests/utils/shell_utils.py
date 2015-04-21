from ucloudclient.client import Client as uclient
import json
cl = uclient(base_url, public_key, private_key)
host = cl.uhost.get(region="us-west-01")
print