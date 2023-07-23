# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-23 12:55
"""
import random
import time


def timer(func):
    """
    装饰器：打印函数耗时
    """

    def decorated(*args, **kwargs):
        st = time.perf_counter()
        print(f'函数:{func}运行前')
        ret = func(*args, **kwargs)
        print(f'函数{func},运行结束')
        print(f"time cost:{time.perf_counter() - st}")

        return ret

    return decorated


# @timer
def random_sleep():
    """随机睡眠一小会"""
    time.sleep(random.random())


random_sleep = timer(random_sleep)
if __name__ == '__main__':
    random_sleep()
