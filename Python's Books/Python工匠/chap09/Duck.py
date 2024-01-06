# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 12:33
"""


class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"Quack! I'm {self.name}!")


class WordyDuck(Duck):
    def quack(self):
        print(f"Quack!Quack!Quack! I'm {self.name}")


if __name__ == '__main__':
    donald = Duck('donald')
    donald.quack()
