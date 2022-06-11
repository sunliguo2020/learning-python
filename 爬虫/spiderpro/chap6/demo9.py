# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/19 13:16
"""
from queue import  Queue
q = Queue(5)
for i in range(4):
    q.put(i)

print(q.qsize())
for _ in range(5):
    print(q.get())
