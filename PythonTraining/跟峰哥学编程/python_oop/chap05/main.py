# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-18 9:23
类方法需要使用@classmethod 装饰器来定义
类方法的第一个参数是类本身
"""
from pprint import pprint


def size(value):
    return value * 1.5


class Student:
    school = 'abc'

    @classmethod
    def get_instance(cls):
        return cls()

    @classmethod
    def say_hello(cls):
        print(f'hello,{cls.__name__}')

    @staticmethod
    def say():
        print('hello')
        print(Student.school)

    def speak(self):
        n = 12
        n = size()
        print(n)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def main():
    student = Student()
    print(type(student))
    student.get_instance()
    student.say_hello()
    s2 = Person('我是谁')
    print(type(s2))
    print(s2)
    # print(type(student))
    # pprint(student.__dict__)

    Student.say()


if __name__ == '__main__':
    main()
