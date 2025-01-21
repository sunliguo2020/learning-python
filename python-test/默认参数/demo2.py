# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-12 7:45
"""


def get_or_create(defaults=None, **kwargs):
    print("defaults", defaults)
    print('kwargs', kwargs)


if __name__ == '__main__':
    item = {'name': 'liguo', 'age': 18}
    idcard = 123456789
    year = 2020
    get_or_create(idcard=idcard, year=year, **item)
