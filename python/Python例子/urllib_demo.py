# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/26 9:11
"""
import urllib.parse
import urllib.request

url = 'http://httpbin.org/post'
post_data = urllib.parse.urlencode({
    'name': "sunliguo",
    "password": "A1234567"
}).encode('utf-8')
print(post_data)
header = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, data=post_data, headers=header)

req.add_header('User-Agent', "Mozilla/5.0 add_header")
resp = urllib.request.urlopen(req)

print(resp.read())

urllib.request.urlretrieve(url="http://www.baidu.com",filename='baidu.text')