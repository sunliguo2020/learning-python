# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/6/6 14:04
"""
import urllib.request
import urllib.parse
url = 'http://www.iqianyue.com/mypost/'

postdata = urllib.parse.urlencode(
    {'name':"ceo@iaianyue.com",
     "pass":'a123456'}
).encode('utf-8')

req = urllib.request.Request(url,postdata)
req.add_header('User-Agent',"Mozilla/5.0")
data = urllib.request.urlopen(req).read()
fhandle = open('./4.5.2.html','wb')
fhandle.write(data)
fhandle.close()