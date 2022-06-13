# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 18:33
"""
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
    loop0()
    loop1()
    print("all done at :", ctime())


if __name__ == '__main__':
    main()
