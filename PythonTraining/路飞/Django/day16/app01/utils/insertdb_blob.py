# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/9 8:11
"""
import os

def file_blob(filename):
    """
    返回文件的二进制
    :param filename:
    :return:
    """
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            blob = f.read()
        return blob
    else:
        return None
