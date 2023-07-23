# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-23 13:16
"""
import random
import time


def timer(print_args=False):
    """
    装饰器：打印函数耗时
    print_args 是否打印方法名和参数，默认为false
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.perf_counter()
            print(f'函数:{func}运行前')
            ret = func(*args, **kwargs)
            print(f'函数{func},运行结束')
            if print_args:
                print(f"{func.__name__},args:{args},kwargs:{kwargs}")
            print(f"time cost:{time.perf_counter() - st}")

            return ret

        return wrapper

    return decorator


@timer(print_args=True)  # _decorator = timer(print_args=True) ramdom_sleep= _decorator(ramdom_sleep)
def random_sleep():
    time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
