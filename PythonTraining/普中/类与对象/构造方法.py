# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-04 7:33
"""
import sys


class Information(object):
    def __init__(self, name, sex):
        print(f"class id(name):{id(name)},{sys.getrefcount(name)}")
        self.name = name
        self.sex = sex
        print(f"self id(name):{id(self.name)},{sys.getrefcount(self.name)}")

        print(name is self.name)

    def info(self):
        print(f"姓名：{self.name}")
        print(f"性别：{self.sex}")


information = Information('小王', '女')

information.info()
