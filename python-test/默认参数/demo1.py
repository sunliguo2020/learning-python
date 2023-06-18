# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/6 18:02
"""


class Person():
    def __init__(self, name, items=None):
        self.name = name
        if items is None:
            print("传入的是None，我要初始化为[]")
            self.items = []
        else:
            print("传入的不是None，还是传来的值！")
            self.items = items
        print(id(self.items))

    def run(self):
        pass


p1 = Person("sunliguo")
p2 = Person('p2')
p3 = Person('p3',"dasf")
print(p1.items)
print(p3.items)