# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-01-07 17:18
"""


class queue():
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        self.list.append(item)

    # 出队
    def dequeue(self):
        self.list.pop(0)

    # 判断是否为空
    def is_empty(self):
        return self.list == []

    # 队列长度
    def size(self):
        return len(self.list)
