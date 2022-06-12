# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 8:35
"""
def get_formatted_name(first_name,last_name):
    """
    返回整洁的姓名
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = f"{first_name} {last_name}"
    return  full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)