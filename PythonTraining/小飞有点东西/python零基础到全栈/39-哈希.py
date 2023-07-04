# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-30 10:08
"""
import hashlib

h1 = hashlib.md5()
h1.update('abc我'.encode('gbk'))
print(h1.hexdigest())

h2 = hashlib.md5()
h2.update('abc我'.encode('utf-8'))
print(h2.hexdigest())

print('我是谁'.encode('utf-8'))