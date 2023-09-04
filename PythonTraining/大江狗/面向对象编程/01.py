# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-15 21:28
"""


class Student:
    # number 属于类变量，定义在方法外，不属于具体实例
    number = 0

    # 定义学生属性，初始化方法
    # name 和 score 属于实例变量，定义在方法里
    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 访问或调用类变量的正确方式是类名.变量名或者self.__class__.变量名。self.__class__自动返回每个对象的类名
        self.__class__.number = self.__class__.number + 1
        print('in __Init__ number:', self.__class__.number)

    # 定义打印学生信息的方法
    def show(self):
        print(f"Name:{self.name}.Score:{self.score}")

    # 定义类方法，打印学生的数量
    @classmethod
    def total(cls):
        print("Total: {0}".format(cls.number))


if __name__ == '__main__':
    student1 = Student('lu', 100)
    student2 = Student('lu', 100)
    Student.total()
    Student.number = 222
    Student.total()
    # Student(student2).show()
    Student.show(student2)
    print(student2.name)
