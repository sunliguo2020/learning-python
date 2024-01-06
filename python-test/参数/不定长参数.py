# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-03 18:36
测试不定长参数
"""


def fun1(f1, f2, f3, f4='123'):
    print(f"f1:{f1}")
    print(f"f2:{f2}")
    print(f"f3:{f3}")
    print(f"f4:{f4}")


def fun2(*args, **kwargs):
    print(f'在fun2中参数args:{args},kwargs:{kwargs}')
    fun1(*args, **kwargs)


if __name__ == '__main__':
    fun2(1, 2, 3, f4='sdf')
