# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/18 10:41
"""
from concurrent.futures import ThreadPoolExecutor


def func(name, t):
    for i in range(10):
        print("我是", name)
    #return name


def fn(res):
    print(res.result())

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as t:
        for i in range(100):
            t.submit(func, f"周杰伦{i}", 2)
