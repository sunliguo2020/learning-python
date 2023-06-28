# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 18:52
"""
import _thread
from time import sleep, ctime


def loop0():
    print("start loop  0 at:", ctime())
    sleep(4)
    print("loop 0 done at:", ctime())


def loop1():
    print("start loop 1 at:", ctime())
    sleep(4)
    print("loop 1 done at:", ctime())


def main():
    print("start at:", ctime())
    # star_ne_thread(function,args,kwargs=None) 派生一个新的线程，使用给定的args和可选的kwargs来执行function
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print("all done at :", ctime())


if __name__ == '__main__':
    main()
