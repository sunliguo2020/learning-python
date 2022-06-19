# -*- coding: utf-8 -*-
'''
Created on 2016-8-11

@author: sunliguo
'''

f = open("D:/id.csv")

for i in f:
    j = i.split(',')
    print j[0],j[1],j[2][:-1]