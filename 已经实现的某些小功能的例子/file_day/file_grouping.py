#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016-7-17
2019-05-14:定义mymovefile函数，删除开始就创建文件夹的语句。
@author: sunliguo
'''
import os
import shutil

def  mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
       fpath,fname = os.path.split(dstfile) #分离文件名和路径
       if not os.path.exists(fpath):
           os.makedirs(fpath)
       if not os.path.isfile(dstfile):
           shutil.move(srcfile,dstfile)
       else:
           print "目的目录已经有同名文件"
           
       print "%s->%s" %(srcfile,dstfile)
           
file_1215=0
file_zero=0
file_428=0
file_414 = 0
file_1000=0

DIR= '../Myfirst/'

fileList = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name)) ]

#统计当前目录下文件的个数
Total = len(fileList)
for i in fileList:
    print "Total:%r" %(Total),
    #print i
    if (i.endswith(".txt") or i.endswith('.xml')):
        fileSize = os.path.getsize(i)
        print "file %s 's size is %r"  % (i,fileSize)
        if  fileSize > 1100:
            mymovefile(i,os.path.join('./1215/', os.path.basename(i)))
            file_1215+=1
        elif fileSize == 0 or fileSize == 160:
            mymovefile(i,os.path.join('./zero/', os.path.basename(i)))
            file_zero+=1
        elif fileSize <= 999:
            mymovefile(i,os.path.join('./414/', os.path.basename(i)))
            file_414+=1
        elif fileSize >=1000:
            mymovefile(i,os.path.join('./1000/', os.path.basename(i)))
            file_1000+=1
    else:
        print "file %s " %(i)
    Total=Total-1
        
print "file_1215  = %r file_zero = %r file_428 = %r file_414= %r file_1000= %r" %(file_1215,file_zero,file_428,file_414,file_1000)
