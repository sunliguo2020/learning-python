#!/usr/bin/env person
#coding:utf-8
'''
person 基础之列表拷贝

'''
a = [1,2,3,40]
#通过内置方法id查看对象的地址
print id(a)
#拷贝一个a的列表，并且赋值给变量b
b = a[:]
print b 
print id(b)

c = a
print id(c)
