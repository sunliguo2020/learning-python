# -*- coding: utf-8 -*-
"""
 @Time : 2022/9/22 19:45
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : rename mail.py
 根据eml文件的MD5值改写文件名。
"""

import os
import logging
import re

from GetFileMd5 import GetFileMd5

logging.basicConfig(filename='rename_eml.log', level=logging.DEBUG,
                    filemode='w',
                    encoding='utf-8',
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(message)s')


def walk_dir(directory):
    """
    :param directory: 遍历文件夹，返回各个文件的路径
    :return:
    """

    if not os.path.isdir(directory):
        print(f"{directory}不是一个目录")
        return -1

    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            # 文件的全路径
            yield os.path.join(root, file)


def rename_eml_file_name(mail_file_path=''):
    """

    @param mail_file_path:要改名的eml文件
    @return:
    """
    if os.path.isfile(mail_file_path) and mail_file_path.endswith('.eml'):

        # 判断一下是不是已经修改了文件名
        file_name = os.path.basename(mail_file_path).replace('.eml', "")
        if re.findall(r"([a-fA-F\d]{32})", file_name) and len(file_name) == 32:
            print(f"{mail_file_path}可能已经修改过文件名！")
            return

        # 获取mail文件的md5值
        md5sum = GetFileMd5(mail_file_path)
        # 文件md5获取失败，则继续
        if md5sum is None:
            logging.debug(f'获取{mail_file_path}的md5值失败!')
            return
        print(mail_file_path, md5sum)

        new_file_name = md5sum + '.eml'
        new_file_path = os.path.join(os.path.dirname(mail_file_path), new_file_name)

        if not os.path.isfile(new_file_path):
            print('准备重命名文件')
            print(f'新的文件名（带路径）：{new_file_path}')
            try:
                os.renames(mail_file_path, new_file_path)
            except Exception as e:
                # print("重命名过程中出错：", e)
                logging.debug(f"重命名{mail_file_path}失败,错误为{e}")
        else:
            logging.debug(f"{os.path.basename(mail_file_path)}已经存在该md5值的文件")


if __name__ == '__main__':
    root_dir = r'F:\eml'
    for item in walk_dir(root_dir):
        rename_eml_file_name(item)
