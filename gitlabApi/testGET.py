import urllib
import urllib2

url = "http://gitlabyang.autoio.org/api/v3/users?private_token=zLRmx2cR5xriFpjZcs95"

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res
