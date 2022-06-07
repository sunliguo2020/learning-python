# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/14 19:02
字符串大小写转换
"""

s = "hello python"
a = s.upper() #转为大写，生成大写字符串
print(a, id(a))
print(s, id(s))

b = s.lower()

print(b,id(b))
print(s,id(s))
print(b is s)

s2 = "hello,Python"
print(s2.swapcase())
print(s2.title())