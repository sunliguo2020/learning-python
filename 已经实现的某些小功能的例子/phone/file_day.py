#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/23 8:04
按照文件的修改日期，分类到各自的日期目录中
"""

import os
import time


def mymove_file(src,dst):
    if not os.path.isfile(src):
        print('%s not exist!'%(src))
    else:
        fpath,fname =os.path.split(dst)
        print(fpath)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        os.rename(src,dst)
        print('move {0}->{1}'.format(src,dst))


#print(os.listdir('./'))
file_list = [i for i in os.listdir('./') if i.endswith('.txt') and os.path.isfile(i)]
file_count = len(file_list)
for file in file_list:
    file_full_path = os.path.join('./',file)
    mtime = os.stat(file_full_path).st_mtime
    '''
    atime = os.stat(file_full_path).st_atime
    ctime = os.stat(file_full_path).st_ctime
    '''
    file_modify_time = time.strftime('%Y-%m-%d',time.localtime(mtime))
    '''file_access_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(atime))
    file_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ctime))
    # print(mtime)'''
    #print(file_full_path,"mtime",file_modify_time)
    '''print(file_full_path, "ctime", file_create_time)
    print(file_full_path, "atime", file_access_time)'''
    #print(type(file_modify_time))
    dstfile = os.path.join('./'+file_modify_time,file)
    print('file_count:{0}'.format(file_count))
    mymove_file(file_full_path,dstfile)
    file_count = file_count - 1
