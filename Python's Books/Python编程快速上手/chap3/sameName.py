# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/29 10:58
"""


def spam():
    eggs = 'spam local'
    print(eggs)


def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


eggs = 'global'
bacon()
print(eggs)
