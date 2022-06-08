# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/23 13:28
"""
fp = open('text.txt','w')
print("奋斗成就更好的你",file=fp)
fp.close()

with open('./text2.txt','w') as f:
    f.write('奋斗成就更好的你')