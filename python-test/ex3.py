# -*- coding: utf-8 -*-

"""
@author: sunliguo

@contact: QQ376440229

@Created on: 2020/3/8 13:04
"""

a="sdfsadf"
print(id(a))
def fu1():
  #  print(id(a))
    a="test a"
    print(a)
    print(id(a))


fu1()
print(id(a))
print(a)