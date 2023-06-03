# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 21:19
"""


class Apple:
    count = 0

    def add_one(self):
        self.count = 1

    @classmethod
    def add_two(cls):
        cls.count = 2


apple = Apple()

apple.add_one()
print(f"Apple.count:{Apple.count}")
print(f"apple.count:{apple.count}")

Apple.add_two()
print(Apple.count)

apple2 = Apple()
print(f'apple2.count:{apple2.count}')