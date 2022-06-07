# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/12 18:26
"""

items = ['Fuits', 'books', 'other']
prices = [96, 78, 85,100,2,3,333]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
