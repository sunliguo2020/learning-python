# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/14 17:51
"""
def func(*args):
    print(args)
    print(*args)
    print("type(args)",type(args))
li=[1,2,3]
func(*li)

def fun3():
    """

    :return:
    """