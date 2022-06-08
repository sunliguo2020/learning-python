# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/27 10:41
"""
import time
from concurrent.futures import ThreadPoolExecutor


def func(name, t):
    # for i in range(10):
    #     print(name, i)
    time.sleep(t)
    print('我是：', name)
    return name


def fn(res):
    print(res.result())


if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        # for i in range(10):
        #     t.submit(func, f"周杰伦{i}",2).add_done_callback(fn)
        #t.map(func, ['周杰伦', '王力宏'], [1, 2])
        t.submit(func,"周杰伦",1)
        t.submit(func,"王力宏",2)


