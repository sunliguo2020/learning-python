# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-23 8:23
"""
from time import ctime, sleep

from MyThread import MyThread


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x - 1)


funcs = [fib, fac, sum]
n = 12


def main():
    nfuncs = range(len(funcs))
    print("**** SINGLE `THREAD")
    for i in nfuncs:
        print(f"staring {funcs[i].__name__},'at:',{ctime()}")
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())


if __name__ == '__main__':
    main()
