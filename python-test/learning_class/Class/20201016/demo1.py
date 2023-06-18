# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/16 20:23
"""


class Person(object):
    def __init__(self,name,age): #初始化函数，
        print(f'__init__方法被调用执行了，self的id值为{id(self)}')
        self.name = 'sdf'
        self.age = 18

    def __new__(cls, *args, **kwargs):
        print(f'__new__方法调用执行了，cls的id值为{id(cls)}')
        obj  = super().__new__(cls) #获取创建的Person类型的（实例）对象
        print(f'创建的对象（obj）的id值为：{id(obj)}')
        return obj

per = Person('jack',20)
print(f'per这个Person类型的实例对象的id值为{id(per)}')

