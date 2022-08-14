# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/4 18:44
"""
import chardet

a = '你好'
b = 'nihao'

a1 = a.encode()
b1 = b.encode()
print(chardet.detect(a1))
print(chardet.detect(b1))

ac = chardet.detect(a1)
print(a1.decode(ac['encoding']))