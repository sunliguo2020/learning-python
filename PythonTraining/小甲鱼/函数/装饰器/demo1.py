# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:52
"""

#
# def myfunc():
#     print("正在调用myfunc...")
#
#
# def report(func):
#     print('主人，我要开始调用函数了')
#     func()
#     print('主人，我调用完函数了')
#
#
# report(myfunc)

import time


def time_master(func):
    def call_func():
        print('开始运行程序')
        start = time.time()
        func()
        end = time.time()
        print('结束程序运行')
        print(f'总共运行了{end - start}秒')

    return call_func


@time_master
def myfunc():
    time.sleep(2)
    print('hello fishc ')


# time_master(myfunc)
myfunc()
