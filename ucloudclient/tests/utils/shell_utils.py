from ucloudclient.client import Client as uclient

cl = uclient(base_url, public_key, private_key)
host = cl.uhost.get(region="us-west-01")
print