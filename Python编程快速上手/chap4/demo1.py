# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/19 21:01
"""
spam =42
print("id(spam)",id(spam))
chess = spam
print("id(chess)",id(chess))
spam = 1000
print("id(spam),spam)",id(spam),spam)
print("id(chess),chess",id(chess),chess)