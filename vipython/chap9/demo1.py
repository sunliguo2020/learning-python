# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/14 19:10
"""
# 字符串的驻留机制
a = 'python'
b = "python"
c = """python"""
print(a, id(a))
print(b, id(b))
print(c, id(c))
