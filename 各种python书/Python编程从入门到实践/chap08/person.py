# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 8:40
"""


def build_person(first_name, last_name, age=None):
    """
    返回一个字典，其中包含有一个人的信息。
    :param first_name:
    :param last_name:
    :param age:
    :return:
    """

    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 30)
print(musician)
