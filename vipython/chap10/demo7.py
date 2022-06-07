# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/17 18:47
"""
def fun(a,b,c):#a,b,c形式参数
    print("a=",a)
    print("b=",b)
    print("c=",c)

fun(10,20,30)#函数调用时的参数传递，位置传参

lst=[11,22,33]
fun(*lst)#函数调用时，将列表中的每个元素都转换为位置实参

fun(a=100,c=300,b=200) #关键值实参

dic = {'a':11,"b":222,"c":333}
fun(**dic) #参数调用时，
