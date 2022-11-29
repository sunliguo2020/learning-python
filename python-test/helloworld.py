#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2016-7-17
2019-05-14:定义mymovefile函数，删除开始就创建文件夹的语句。
2019-11-15:修改为python3版本

@author: sunliguo
"""

import os
import shutil

file_1215 = 0
file_zero = 0
file_414 = 0
file_1000 = 0

DIR = './'


# 移动文件到指定的目录中
def Move_File(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        if not os.path.isfile(dstfile):
            shutil.move(srcfile, dstfile)
        else:
            print("目的目录已经有同名文件")

    print("%s->%s" % (srcfile, dstfile))


# 按照文件大小分类
def Fenlei_file(srcfile):
    global file_1000, file_1215, file_414, file_zero

    if (srcfile.endswith(".txt") or srcfile.endswith('.xml')):
        file_size = os.path.getsize(srcfile)
        print("file %s 's size is %r" % (srcfile, file_size))
        if file_size >= 1100:
            Move_File(srcfile, os.path.join('./1215/', os.path.basename(srcfile)))
            file_1215 += 1
        elif file_size == 0 or file_size == 160:
            Move_File(srcfile, os.path.join('./zero/', os.path.basename(srcfile)))
            file_zero += 1
        elif file_size <= 999:
            Move_File(srcfile, os.path.join('./414/', os.path.basename(srcfile)))
            file_414 += 1
        elif file_size >= 1000:
            Move_File(srcfile, os.path.join('./1000/', os.path.basename(srcfile)))
            file_1000 += 1
    else:
        print("file %s " % (srcfile))


# 统计当前目录下的文件到列表中
fileList = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]

# 统计当前目录下文件的个数
Total = len(fileList)
"""
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(a),3):
    b=a[i:i+3]
    print b
    

[a[i:i+3] for i in xrange(0,len(a),3)]
"""
for i in fileList:
    print("Total:%r\t" % (Total), end="")

    Fenlei_file(i)
    Total = Total - 1

print("file_1215  = %r file_zero = %r file_414= %r file_1000= %r" % (
    file_1215, file_zero, file_414, file_1000))
