# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/20 17:49
"""

import csv

csvfile  = open('../data/chp3/data-text.csv','r')
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)
