# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 20:15
"""
import json

dic = {
    'hobby':['football','pingpang','smoke'],
    'age':20,
    "score":97.6,
    "name":"zhangsan"
}
print("type(dic)",type(dic))
r   = json.dumps(dic)
print(r)
print(type(r))