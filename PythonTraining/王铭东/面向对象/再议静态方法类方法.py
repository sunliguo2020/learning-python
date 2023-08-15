# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-14 13:39
实例方法：由对象调用，至少一个self参数，执行实例方法时，自动将调用该方法的对象赋值给self
类方法：由类调用，至少一个cls参数，执行类方法时，自动将调用该方法的类赋值给cls
静态方法：由类调用，无默认参数。
"""


class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """
        定义实例方法，至少有一个self参数
        """
        # print(self.name)

        print('实例方法')

    @classmethod
    def class_func(cls):
        """
        定义类方法，至少有一个cls参数
        """
        print('类方法')

    @staticmethod
    def static_func():
        """
        定义静态方法，无默认参数
        """
        print('静态方法')


if __name__ == '__main__':
    a = Foo("who")
    a.ord_func()
    a.class_func()
    a.static_func()
    print("*"*33)
    # Foo('2').name
    # Foo().class_func()