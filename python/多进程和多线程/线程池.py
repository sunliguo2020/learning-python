# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/25 15:54
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep
import threading

def fn(arg1, arg2, arg3=[]):
    print(f'我是线程{threading.current_thread().name} ，我要睡觉了')
    sleep(arg1)
    print("我睡醒了，", arg1, arg2, arg3)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=300,thread_name_prefix='sun') as executor:
        for i in range(1000):
            executor.submit(fn, randint(0, 10), {"key": "sunliguo"})
            # executor.map()
            #.done() 判断线程是否结束  

            # .result() 返回
