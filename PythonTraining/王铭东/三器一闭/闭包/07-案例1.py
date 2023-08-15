# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 18:56
"""


def test(number):
    def test_in(number_in):
        print(f"in test_in 函数，number_in is {number_in}")
        return number + number_in

    return test_in


ret = test(20)
print(ret(100))
print(ret(200))
