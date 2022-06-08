# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/15 19:47
"""
with open('../myfun2.py') as f:
    print(dir(f))
    for i in f:
        print(i,end='')