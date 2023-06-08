# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-05 12:42
"""
from urllib.request import urlopen

img_url = 'https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF'
result = urlopen(img_url)
print(type(result)) # <class 'http.client.HTTPResponse'>

# TypeError: a bytes-like object is required, not 'HTTPResponse'
"""
with open('a.gif','wb') as fp:
    fp.write(result)
    
    """
with open('a.gif','wb') as fp:
    fp.write(result.read())