# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/24 12:41
"""
import os
import csv
from datetime import datetime


def walk_dir(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


file_name = '10.155.88.254_20220624110506_arp.log'
dir_path = r'D:\睿智\国土局\政务网\10.155.88.254_arp\202204'
line_list = []
count = 0

for file_path in walk_dir(dir_path):
    count += 1
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
    #文件名包含手机mac地址的时间
=======
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172
=======
>>>>>>> 784558807086f17f7daecab3309a3392ab8b04c8
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
    file_time = os.path.basename(file_path).split('_')[1]
    file_date_obj = datetime.strptime(file_time, '%Y%m%d%H%M%S')

    print(count, file_time, len(line_list))
    with open(file_path) as fp:
        for line in fp:
            new_line_text = line.split()
            if len(new_line_text) == 6:
                # print(new_line)
                del new_line_text[2]
                new_line_text.insert(0, file_date_obj)
                # if new_line_text[:4] not in line_list:
                line_list.append(new_line_text[:4])

<<<<<<< HEAD
with open('ip_arp_202204.csv', 'w', newline='') as fp:
=======
<<<<<<< HEAD
<<<<<<< HEAD
with open('ip_arp_202204-2.csv', 'w', newline='') as fp:
=======
with open('ip_arp_202204.csv', 'w', newline='') as fp:
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172
=======
with open('ip_arp_202204.csv', 'w', newline='') as fp:
>>>>>>> 784558807086f17f7daecab3309a3392ab8b04c8
>>>>>>> 3834090fde219e5410786a486c94f6cf2329ea24
    csv_write = csv.writer(fp)
    csv_write.writerows(line_list)
