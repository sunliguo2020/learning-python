# -*- coding: utf-8 -*-
'''
 @Time : 2022/5/28 22:16
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : sun_tool.py
 @Project : pycharm
'''
import hashlib
import os
import datetime


def get_file_md5sum(filename):
    if not os.path.isfile(filename):
        return -1
    myhash = hashlib.md5()

    with open(filename, 'rb') as f:
        while True:
            b = f.read()
            if not b:
                break
            myhash.update(b)

    return myhash.hexdigest()


def walk_dir(dir):
    """
    遍历文件夹，返回各个文件的路径
    :param dir:
    :return:
    """

    if not os.path.isdir(dir):
        print(f"{dir}不是一个目录")
        return -1
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path
