# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-01-04 18:41
"""
from Crypto.Cipher import DES,DES3
from Crypto.Util.Padding import  pad
des = DES.new(key=b'abcdefgs',mode=DES.MODE_CBC,IV=b'ij2h3bd3')


s = '你好啊'.encode('utf-8')
s = pad(s,8)
bs = des.encrypt(s)
print(bs)