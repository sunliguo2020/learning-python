# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/25 15:54
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep


def fn(arg1, arg2, arg3=[]):
    print('我是线程，我要睡觉了')
    sleep(arg1)
    print("我睡醒了，", arg1, arg2, arg3)


if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        for i in range(1000):
            executor.submit(fn, randint(0, 10), {"key": "sunliguo"})
