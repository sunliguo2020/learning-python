# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/5/30 18:26
"""
import urllib.request
import urllib.parse
keyword='孙立国'
key_code = urllib.parse.quote(keyword)
url = 'http://www.baidu.com/s?wd='+key_code
req = urllib.request.Request(url)
data =urllib.request.urlopen(req).read()
fhandle = open('./4.html','wb')
fhandle.write(data)
fhandle.close()