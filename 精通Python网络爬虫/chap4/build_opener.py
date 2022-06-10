# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 19:53
"""
import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/deails/5118226"
headers=("User-Agent","Mozilla/4.0 (Windows NT 6.1; WOW64) AppleWebkit/537.36")

opener =urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
print(data)
