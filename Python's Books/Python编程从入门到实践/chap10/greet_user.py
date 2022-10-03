# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2021/2/12 14:34
"""
import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"We'll back,{username}")
