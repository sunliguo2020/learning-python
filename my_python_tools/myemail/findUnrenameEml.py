# -*- coding: utf-8 -*-
"""
 @Time : 2023/3/3 21:44
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : findUnrenameEml.py
 @Project : learning-python
"""
import os.path
import re
import shutil

if __name__ == '__main__':
    eml_path = r"f:\eml_new"
    new_eml_path = r'f:\email'

    for root, dirs, files in os.walk(eml_path, topdown=False):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not filename.endswith('.eml'):
                continue
            file_name = filename.replace('.eml', '')
            if not re.findall(r"([a-fA-F\d]{32})", file_name) or len(file_name) != 32:
                print(f'准备移动{filename}')
                try:
                    shutil.move(file_path, new_eml_path)
                except Exception as e:
                    print(f'移动过程中出错,{e}')
            else:
                print(f"{filename}已经改过名了！")
