# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 13:03
"""
import random


class Duck:
    def __init__(self, color):
        self.color = color

    def quack(self):
        print(f"Hi,I'm a {self.color} duck!")

    @classmethod
    def create_random(cls):
        """创建一只颜色随机的鸭子"""
        color = random.choice(['yellow', 'white', 'gray'])
        return cls(color=color)


if __name__ == '__main__':
    d = Duck.create_random()
    d.quack()
