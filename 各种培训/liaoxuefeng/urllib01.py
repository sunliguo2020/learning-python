# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/3/15 11:23
"""
from urllib import request

with request.urlopen("http://api.douban.com/v2/book/2129650") as f:
    data = f.read()
    print('status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print ('Data:',data.decode('utf-8'))