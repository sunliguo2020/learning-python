#!/usr/bin/person
# -*- coding: utf-8 -*-
'''
Created on 2016-7-17

@author: sunliguo
'''
import os
import shutil


file_1215=0
file_zero=0
file_428=0
file_414 = 0

if not os.path.isdir('./1215'):
    os.mkdir('./1215')
if not os.path.isdir('./zero'):
    os.mkdir('./zero') 
if not os.path.isdir('./428'):
    os.mkdir('./428')  
if not os.path.isdir('./414'):
    os.mkdir('./414')
   
fileList = os.listdir('./')
#print 'the number of ./ is %r' % len(fileList)

'''   
txtFileList = []
for j in fileList:    
    if os.path.isfile(j) and j.endswith('.txt'):
        print j
        txtFileList.append(j)'''
#Total = len(fileList)
Total = len(fileList)

for i in fileList:
    if os.path.isfile(i) and (i.endswith(".txt") or i.endswith('.xml')):
        fileSize = os.path.getsize(i)
        print "Total:%r :file %s 's size is %r"  % (Total,i,fileSize)
        if  fileSize > 1201:
            os.rename(i,os.path.join('./1215/', os.path.basename(i)))
            #shutil.move(i,'./1215/')
            file_1215+=1
        elif fileSize == 0:
            os.rename(i,os.path.join('./zero/', os.path.basename(i)))
            file_zero+=1
        elif fileSize == 428:
            os.rename(i,os.path.join('./428/', os.path.basename(i)))
            file_428+=1
        elif fileSize <= 500:
            os.rename(i,os.path.join('./414/', os.path.basename(i)))
            file_414+=1
    Total=Total-1
        
print "file_1215  = %r file_zero = %r file_428 = %r file_414= %r" %(file_1215,file_zero,file_428,file_414)