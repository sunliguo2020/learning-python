# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/22 7:34
"""
print(dir(object.__dict__))
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = C("Jack",29)
print(x.__dict__)
print(C.__dict__)
print(x.__class__)
print(C.__bases__)
print(C.__mro__)