# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 21:37
"""

class Felines:
    def feature(self):
        print('猫科动物特长时爬树')


class Cat(Felines):
    name = '猫'

    def feature(self):
        print(f"{self.name}会抓老鼠")
        print(f"{self.name}会爬树")
        print("-"*20)
        super().feature()

cat = Cat()
cat.feature()