# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-17 21:56
类--是描述一类对象的特征集合
对象--是符合类定义特征的具体实例

属性--分为类属性和实例属性
    汽车的颜色
    类属性 奥迪汽车类  生产厂家=奥迪
    变量
    静态特征
方法--分为类方法和实例方法
        动态特征
        函数

"""


class Student:
    pass


class Person:
    pass


def main():
    print(Student)
    print(Person)
    # <class '__main__.Student'>
    print(id(Student))

    # 使用类名+括号  变量存储的地址
    student1 = Student()

    print(isinstance(student1, Student))
    print(isinstance(student1, Person))
    print(isinstance(Student, type))

    print(type(Student))
    print(student1)
    # <__main__.Student object at 0x00000145FBBB7EE0>
    # print(hex(id(student1)))

    student1 = Student()
    print(id(student1))


if __name__ == '__main__':
    main()
