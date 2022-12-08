# -*- coding: utf-8 -*-
'''
Created on 2016-7-30
类属性，实例属性,对象属性
@author: sunliguo
'''
class InstCt(object):
    count = 0
    print "id(count) %s" %id(count)
    def __init__(self):
        print "正在初始化 %s " % self
        
        InstCt.count += 1
        print "InstCt.count id %s" % id(InstCt.count)
        pass
    def __del__(self):
        InstCt.count -= 1
    def howMany(self):
        return InstCt.count
'''    
a = InstCt()
print a.howMany()
b = InstCt()
print b.howMany()

print "*"*50
class ClassB(object):
    count = 0
    def __init__(self):
        print "正在初始化 %s " % self
        self.count += 1
        pass
    def __del__(self):
        self.count -= 1
    def howMany(self):
        return self.count
a = ClassB()
print a.howMany()
b = ClassB()
print b.howMany()'''
