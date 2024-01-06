# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 7:18
"""
import time


class FibInterator(object):

    def __init__(self):
        self.num1 = 0
        self.num2 = 1
        self.item_index = 0

    def __next__(self):
        self.temp = self.num1
        self.num1, self.num2 = self.num2, self.num1 + self.num2
        return self.temp

    def __iter__(self):
        return self


if __name__ == '__main__':
    a = FibInterator()
    print(type(a), a.__dict__)
    for item in a:
        print(item)
        print(type(a), a.__dict__)
        time.sleep(1)
