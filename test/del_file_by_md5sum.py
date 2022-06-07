# -*- coding: utf-8 -*-
'''
 @Time : 2022/5/28 22:18
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : del_file_by_md5sum.py
 @Project : pycharm
'''
import os.path

from sun_tool import get_file_md5sum
from sun_tool import walk_dir
from concurrent.futures import ThreadPoolExecutor


def del_file_by_md5sum(file_path, md5sum):
    if get_file_md5sum(file_path) == md5sum:
        print(f"发现该md5值的文件！{file_path}")
        os.remove(file_path)
        if not os.path.isfile(file_path):
            print("删除成功！")


if __name__ == '__main__':
    with ThreadPoolExecutor(100) as t:
        for file_path in walk_dir(r'F:\pycharm\ShouGuangYun\shebao'):
            print(file_path)
            t.submit(del_file_by_md5sum, file_path, 'd1910f62bb4343bb4892438b43bced50')
