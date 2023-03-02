# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-18 9:12
私有属性和函数
"""


class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def __change_gender(self, gender):
        self.__gender = gender

    def say_hello(self, msg):
        print(f'{msg},{self.__gender}')


def main():
    s1 = Student('jack', '男')
    print(s1.__dict__)
    print(s1._Student__gender)
    s1.say_hello('乌鸦')


if __name__ == '__main__':
    main()
