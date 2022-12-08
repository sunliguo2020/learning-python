# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/8 18:19
"""
import csv
import os
import datetime

csv_rows = []
for root, dirs, files in os.walk('./static/webcam'):
    print(root, os.path)
    for item in files:
        file_name = item
        file_path = os.path.join(root, item).replace('./static/webcam', "")
        print(file_path)
        ipaddr = file_name.split('_')[0]
        print(ipaddr)
        capture_time_str = file_name.split('_')[4]
        # print(capture_time)
        capture_time = datetime.datetime.strptime(capture_time_str, '%Y%m%d%H%M%S')
        print(capture_time)
        csv_rows.append((ipaddr, file_name, capture_time, file_name))

    with open('./webcam.csv', 'a',newline='') as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerows(csv_rows)
