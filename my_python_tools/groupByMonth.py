#!/usr/bin/python
# coding:utf-8
import os

'''
将指定文件夹中的文件按照文件的修改时间分组。每个月份为一个文件夹。
'''
import time
import shutil

# 遍历文件夹获取文件列表。包含所有文件路径的列表。
# filePathList = []

pwd = os.getcwd()
# print(pwd)

for parent, dirnames, filesnames in os.walk(pwd):
    # print(parent,dirnames,filesnames)
    for files in filesnames:
        file = os.path.join(parent, files)
        #文件创建的年和月份
        monthDir = time.strftime('%Y%m', time.gmtime(os.path.getmtime(file)))

        # 创建年月的文件夹
        if monthDir not in os.listdir('../python-test/'):
            os.mkdir(monthDir)
        # 判断是否有重名的文件
        if not os.path.isfile('./' + monthDir + '/' + os.path.basename(file)) and os.path.isdir(
                os.path.join('../python-test/', monthDir)):
            # print(monthDir)
            print('move' + './' + monthDir + '/' + os.path.basename(file))
            shutil.move(file, './' + monthDir)
        else:
            print("same file:", os.path.basename(file))
