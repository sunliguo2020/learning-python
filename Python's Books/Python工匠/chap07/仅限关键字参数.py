# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-22 10:51
"""


def query_users(limit, offset, *, min_followers_count, include_profile):
    pass


#  TypeError: query_users() takes 2 positional arguments but 4 were given
try:
    query_users(200, 0, 100, True)
except TypeError as e:
    print(e)

query_users(20, 0, min_followers_count=100, include_profile=True)
