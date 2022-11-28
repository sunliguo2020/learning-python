# -*- coding: utf-8 -*-
'''
Created on 2016-7-30

@author: sunliguo
'''
class ClassA:
    count = 1
    print "id(count)=%s " % id(count)
    print "id(ClassA.count)=%s " % id(ClassA.count)
    def __init__(self,co):
        self.co = co
        print "id(self.co) = %s" % id(self.co)


a = ClassA(1)
b = ClassA(2)
    