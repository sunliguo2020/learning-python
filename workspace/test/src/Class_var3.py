# -*- coding: utf-8 -*-
'''
Created on 2016-7-31

@author: sunliguo
'''
class Dog:
    tricks = ["init"]
    print locals()
    def __init__(self,name):
        self.name = name
    def add_trick(self,trick):
        print self.tricks
        print "=="*20
        print locals()
        self.tricks.append(trick)
        print locals()
    print "*"*50
    print locals()    
d = Dog("Role")
#print d.tricks
d.add_trick("sdfasf")

print d.tricks

c = Dog("hello")

print c.tricks