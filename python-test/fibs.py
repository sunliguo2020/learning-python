# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/26 13:06
"""


class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000000:
            raise StopIteration
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
# print(type(fibs))
# print(dir(fibs))

print(list(fibs))
# for f in fibs:
#     if f > 100:
#         print(f)
#         print(list(fibs))
#         break
