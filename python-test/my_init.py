# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/24 18:08
"""


class FooBar():
    def __init__(self, var=42):
        self.somevar = var


f = FooBar('dsfasf')
print(f.somevar)


class A():
    def hello(self):
        print("hello,I'm in A")


class B(A):
    def hello(self):
        print("hello, I'm in B")


a = A()
b = B()
a.hello()
b.hello()
