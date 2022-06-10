# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/5/30 21:36
"""

def test_args(first,*args):
    print("type(args):",type(args))

    print(first)
    print(args)

    for item in args:
        print(item)

test_args(1,2,3,4,5)

def test_kwargs(first,*args,**kwargs):
    print('type(kwargs):',type(kwargs))

    print(args)
    print(kwargs)
    print(first)

# test_kwargs(1,2,3,4,a=1,b=2)
a = (22,33,44)
test_kwargs(1,a)