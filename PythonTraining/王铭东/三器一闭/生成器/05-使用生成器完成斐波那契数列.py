# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 7:35
只要一个函数中有yield关键字就生成器。
"""
import time


def fib_generator():
    num1 = 1
    num2 = 1
    while True:
        temp_num = num1
        num1, num2 = num2, num1 + num2
        # return temp_num
        yield temp_num


if __name__ == '__main__':
    for item in fib_generator():
        print(item)
        time.sleep(1)
