'''
Created on 2016-4-18

@author: Administrator
'''

import urllib2
url = "http://www.sunliguo.com"
response = urllib2.urlopen(url)
code = response.getcode()
print type(response)
print code
count = response.read()
#print count.decode('gbk').encode('utf-8')

request = urllib2.Request(url)

request.add_data('addss')
request.add_header('User-agent','Mozilla/5.0')

response = urllib2.urlopen(request)

print response.read()
