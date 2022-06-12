# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/22 19:12
"""


class Student:
    navive_place = '吉林'  # 直接写在类里的属性，称为类属性。

    def __init__(self, name, age):
        self.name = name  # self.name 实例属性
        self.age = age

    # 实例方法
    def eat(self):  # 实列方法
        print("学生在吃饭----")

    # 静态方法
    @staticmethod
    def method():
        print("我使用了staticmethod，进行修饰，所以我是静态方法")

    @classmethod
    def cm(cls):
        print("我是类方法，我使用了classmethod进行修饰")


print(type(Student))
print(id(Student))
print(Student)
print(dir(Student))


def drink():
    print("喝水")
    pass

stu1 = Student("张三",29)
print(id(stu1))
print(type(stu1))
print(stu1)
print("-"*100)
print(id(Student))
print(type(Student))
print(Student)