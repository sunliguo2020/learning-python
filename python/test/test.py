# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/20 8:34
"""
import csv

new_csv = []
with open(r'd:\BaiduNetdiskDownload\导入\csv\130-sortu.csv',encoding='utf-8') as fp:
    csv_reader = csv.reader(fp)
    count = 0
    for line in csv_reader:
        line.insert(0,count)
        print(line)
        new_csv.append(line)
        count += 1

with open('new_csv.csv','w',encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(new_csv)