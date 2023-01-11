# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-09 13:26
"""


def myfunc(a, *args, **kwargs):
    print(a,args,kwargs)


myfunc(1,1, c=2,d=4)
