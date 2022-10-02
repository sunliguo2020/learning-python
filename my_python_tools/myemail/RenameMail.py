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
    root_dir = r'F:\eml_new'
    count = 0
    for (root, dirs, files) in os.walk(root_dir):

        for filename in files:
            if filename.endswith('.eml'):
                count = count + 1
            mail_file_path = os.path.join(root, filename)
            md5sum = GetFileMd5(mail_file_path)
            # 文件md5获取失败，则继续
            if md5sum is None:
                continue
            print(count, mail_file_path, md5sum)

            new_file_name = md5sum + '.eml'
            new_file_path = os.path.join(root, new_file_name)
            print(f'新的路径名：{new_file_path}')

            if not os.path.isfile(new_file_path):
                print('准备重命名文件')
                try:
                    os.renames(mail_file_path, new_file_path)
                except Exception as e:
                    print("重命名过程中出错：",e)
