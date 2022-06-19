# -*- coding: utf-8 -*-
'''
Created on 2016-7-31

@author: sunliguo
'''
def f1(x):
    a = x
    print "a = ",a
    print locals()
    
def f2(y):
    global b
    b = y
    print "b = ",b
    print locals()
    
f1("hello")
f2("world")

#print locals()

def outer():
    a_var = "enclosed value"
    print a_var
    def inner():
        a_var="local value"
        print(a_var)
    inner()
    print a_var
outer()