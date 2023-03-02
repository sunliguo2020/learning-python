# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-23 13:17
将采集的arp表分析，只保留最新的那一条数据
"""
import pandas as pd

dataFrame = pd.read_csv(r'd:\ip_arp.csv', header=None,
                        names=['ip_addr', 'mac_addr', 'interface', 'cap_datetime'])
print(type(dataFrame))
group = dataFrame.groupby(['ip_addr', 'mac_addr', 'interface'])
print(type(group))
# print(len(group.agg('max')))
data = group.agg('max')

data.to_csv('ip-arp-sing.csv')
