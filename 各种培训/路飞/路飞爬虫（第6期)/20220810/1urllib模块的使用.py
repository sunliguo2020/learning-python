# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-08-10 20:54
"""
import urllib.request
url = 'http://www.baidu.com'
# print(url)
#请求网址

res = urllib.request.urlopen(url)
# print(res)
# print(type(res))
print(res.getcode())
print(res.geturl())
print(res.getheaders())
# print(res.read().decode('utf-8'))
