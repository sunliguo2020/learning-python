# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-29 10:20
"""


class People():
    def run(self):
        print("run")

    def talk(self):
        print("talk")


class DriverMixin():
    def driver(self):
        print("driver")


class Children(DriverMixin, People):
    pass


c = Children()
c.run()
c.talk()
c.driver()
