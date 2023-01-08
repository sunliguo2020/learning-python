# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-05 7:53
"""


class A:
    foo = 'xxx'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        pass


print(dir(A))
print(type(A.foo))
print(A.__dict__)
