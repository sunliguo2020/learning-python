# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/22 17:56
"""

def get_count(s,ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1