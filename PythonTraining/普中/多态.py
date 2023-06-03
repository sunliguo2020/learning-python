# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 21:41
"""


class Animal(object):
    def move(self):
        pass


class Rabbit(Animal):
    def move(self):
        print("兔子蹦蹦跳跳")


class Snail(Animal):
    def move(self):
        print("蜗牛缓慢爬行")


def test(obj):
    obj.move()


rabbit = Rabbit()
test(rabbit)

snail = Snail()
test(snail)
