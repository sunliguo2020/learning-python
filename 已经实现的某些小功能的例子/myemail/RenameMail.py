# -*- coding: utf-8 -*-
"""
 @Time : 2022/9/22 19:45
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : rename mail.py
 根据eml文件的MD5值改写文件名。
"""

from GetFileMd5 import GetFileMd5
import os

if __name__ == '__main__':
    root_dir = r'F:\eml'
    count = 0
for (root, dirs, files) in os.walk(root_dir):

    for filename in files:
        if filename.endswith('.eml'):
            count = count + 1
        mail_file_path = os.path.join(root, filename)
        md5sum = GetFileMd5(mail_file_path)
        print(count, mail_file_path, md5sum)
        new_file_name = md5sum + '.eml'
        new_file_path = os.path.join(root_dir, new_file_name)
        print(new_file_path)
        os.renames(mail_file_path, new_file_path)
