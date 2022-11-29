# -*- coding:utf-8 -*-
'''
Created on 2016-7-18
是
@author: sunliguo
'''
import sys
import os

print sys.getdefaultencoding()

#print os.listdir("./")
f = open("D:\\workspace\\test\\src\\zh.txt",'r')
content = f.read()
f.close()

#print content.decode('gbk').encode('utf-8')

try :
    open("abc.txt","r")
except IOError,e:
    print e