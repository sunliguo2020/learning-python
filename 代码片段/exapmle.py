# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/5/30 12:22
"""
import chardet


def file_content(filename):
    # 检测文件的编码
    with open(filename, 'rb') as fp:
        content = fp.read()
    file_encoding = chardet.detect(content)['encoding']

    # with open(file_path,encoding='utf-16-le') as fp:
    with open(filename, encoding=file_encoding) as fp:
        content = fp.readlines()

    return content
