# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/16 20:55
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stuno):
        #super().__init__(name, age)  # 调用父类的初始化函数
        Person.__init__(self,name,age)
        self.stuno = stuno

    def show(self):  # 方法重写
        super().show()
        print(self.stuno)

#创建对象并调用对象的实例方法show()
stu = Student('jack', 20, '10001')
stu.show()

class Sing(object):
    def __init__(self,song_name):
        self.song_name= song_name
    def singing(self):
        print('唱了一首《',self.song_name,'的歌曲')

class Student2(Person,Sing):
    def __init__(self,name ,age ,stuno,song_name):
        super().song_name
        pass
