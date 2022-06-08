# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/29 11:00
"""
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)