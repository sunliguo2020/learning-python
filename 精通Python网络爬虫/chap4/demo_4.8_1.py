# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/5/30 18:55
"""
import urllib.request
import urllib.error

try :
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    print(e.errno)
    print(e.reason)