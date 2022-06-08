# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/14 8:54
"""


def outer(f):
    def inner(*args, **kwargs):
        print("我是个装饰器，我的参数f是：", f)
        ret = f(*args, **kwargs)
        return ret

    return inner


@outer
def fn(name, password):
    print("username,password", name, password)
    print("aaa")

    return "一把屠龙刀"


ret = fn("admin", "12345")
print(ret)
