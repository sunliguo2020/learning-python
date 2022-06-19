# -*- coding: utf-8 -*-
'''
Created on 2016-7-20

@author: sunliguo
'''
xmlfile = open("2333244.txt")
print xmlfile.read().decode('gb2312').encode('utf-8').replace('GB2312','utf-8')