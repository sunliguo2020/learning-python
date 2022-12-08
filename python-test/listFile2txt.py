#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016-7-18
@author: sunliguo
'''
import os

'''
def listFile2txt(dir,file,wildcard=".txt",resursion=0):
    #exts = wildcard.split(" ")
    count=0
    files = os.listdir(dir)
    for name in files:
        if os.path.isfile(name) and name.endswith(wildcard):
            file.write(name+'\n')
            count = count +1
            print count,name      '''

file = open("outfile", "w+")

# listFile2txt(dir,file)
filelist = os.walk("./").next()[2]

file.write(repr(filelist).replace("', '", '\n').replace("['", "").replace("']", ""))
file.seek(0)
# print "len = ",len(file.readlines())
j = 1
for i in file.readlines():
    print(j, i.replace("\n", ''))
    j = j + 1
    file.close()
