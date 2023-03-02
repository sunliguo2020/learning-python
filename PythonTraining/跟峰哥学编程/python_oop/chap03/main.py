# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-17 21:39
实例函数与实例变量
在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型：
类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量。
"""
from pprint import pprint


class Student:
    # 实例函数
    def __init__(self, name):

        # 定义实例变量 ,属于对象
        self.name = name

    def say_hello(self, msg):
        print(f"hello{msg},{self.name}")


def main():
    # 1、create a physical object
    # call __init__() to initialize this object
    s1 = Student("jack")
    s2 = Student('Tom')

    s1.say_hello('hello')
    s2.say_hello('sfda')

    s1.gender = 'Male'
    print(s1.gender)
    pprint(s1.__dict__)
    # print(s2.gender)

    Student.say_hello(s1, 'sdfa')


if __name__ == '__main__':
    main()
