# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/16 13:01
"""
def greet_users(names):
    """
    向列表中的每位用户发出简单的问候。
    :param names:
    :return:
    """
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)