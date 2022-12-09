# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 15:00
"""
import hashlib
from django.conf import settings


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


def file_md5sum(filename):
    """
    返回文件的md5值
    :param filename:
    :return:
    """
    with open(filename, 'rb') as fp:
        f_content = fp.read()
        fmd5 = hashlib.md5(f_content)
    return fmd5.hexdigest()
