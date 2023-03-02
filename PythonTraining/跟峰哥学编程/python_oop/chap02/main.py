# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-17 22:09
什么是类变量？
属于类本身这个对象的属性
所有该类的对象都共享类变量
"""
from pprint import pprint


class Student:
    student_count = 10  # 类变量


def main():
    print(Student.__name__)

    print(Student.student_count)
    print(getattr(Student, 'student_count'))
    print(getattr(Student, 'unknown', '121212'))

    Student.student_count = 100
    print(Student.student_count)
    setattr(Student, 'student_count', 'afwodj')
    print(Student.student_count)

    # 类变量可以动态添加
    Student.new_attr = 'new_attr'
    print(Student.new_attr)
    # __dict__ 查看对象内部所有属性名和属性值组成的字典
    pprint(Student.__dict__)

    del Student.new_attr
    # delattr(Student, 'new_attr')

    # print(Student.new_attr)

    s1 = Student()
    s2 = Student()
    Student.student_count = 1121212
    print(s1.student_count)

    pprint(Student.__dict__)


if __name__ == '__main__':
    main()
