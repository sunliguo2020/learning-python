# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 21:16
"""


class Test:
    @classmethod
    def use_classmet(cls):
        print("我是类方法")


test = Test()

test.use_classmet()
Test.use_classmet()
