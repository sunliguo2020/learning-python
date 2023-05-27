# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-05-25 22:34
"""
class Student(object):
    """学生管理系统"""
    def __init__(self):
        self.stus = []

    def add(self):
        """添加一个新学生"""
        name = input("请输入新学生的姓名:")
        tel = input("学生的手机号：")

        new_stu = dict()
        new_stu['name'] = name
        new_stu['tel'] = tel

        self.stus.append(new_stu)

    def __iter__(self):
        return self.stus


stu_sys = Student()
stu_sys.add()
stu_sys.add()
stu_sys.add()

for temp in stu_sys:
    print(temp)