# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/17 18:37
"""


def fun(*args):  # 函数定义时，位置参数
    print(args)


fun(1, 2, 3, 3)
fun(10, )
fun(10, 20, 30)


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=20, b=30, c=40)
print()
"""
def fun2(*args,*a):
    pass
    以上代码，程序会出错，可变位置参数，只能是1个
    """