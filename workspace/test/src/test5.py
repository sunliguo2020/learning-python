# -*- coding: utf-8 -*-
'''
Created on 2016-7-18

@author: sunliguo
'''
class MyError(Exception):
    print 22
try :
    raise  MyError
except MyError:
    print "yic"