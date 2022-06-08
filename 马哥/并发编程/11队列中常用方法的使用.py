# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 20:56
"""
from multiprocessing import Queue

q = Queue(3)
q.put("消息1")
q.put("消息2")
q.put("消息3")
# q.put("消息4",block=True,timeout=1)
print("判断当前队列是否已满：", q.full())

if not q.full():
    q.put("消息4", block=True, timeout=1)
print(q.get())
print(q.get())
print(q.get())
if not q.empty():
    print(q.get(block=True, timeout=1))

# 查看队列的大小
print("队列的大小", q.qsize())
