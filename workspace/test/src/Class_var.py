# -*- coding: utf-8 -*-
'''
Created on 2016-7-31

@author: sunliguo
'''
class A:
    aa =0 

class B:
    def __init__(self):
        bb = 0
        
class C:
    def __init__(self):
        self.cc =0
 
a = A()
b = A()


print A.aa

A.aa =100000
        

print a.aa
a.aa +=1 
print a.aa

print "="*50

print b.aa
print A.aa