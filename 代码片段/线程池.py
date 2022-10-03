# -*- coding: utf-8 -*-
"""
 @Time : 2022/10/2 19:15
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : 线程池.py
 @Project : github
"""
from concurrent.futures import ThreadPoolExecutor


def fun1(arg1, arg2):
    pass


if __name__ == '__main__':
    with ThreadPoolExecutor() as t:
        for arg1,arg2 in [[0]*2]*4:
            print(arg1,arg2)
            t.submit(fun1, arg1,arg2)
