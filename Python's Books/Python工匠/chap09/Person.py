# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 12:39
"""


class Person:
    """
    一个“人”类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"Hi,My name is {self.name},I'm {self.age}")

    def __setattr__(self, name, value):
        # 不允许设置年龄小于0
        if name == 'age' and value < 0:
            raise ValueError(f"Invalid age value:{value}")
        super().__setattr__(name, value)


if __name__ == '__main__':
    p = Person('raymod', 30)
    print(p.__dict__)
    print(Person.__dict__)
    p.age = -3
