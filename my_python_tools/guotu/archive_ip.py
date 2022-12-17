# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/24 12:41
将采集到arp表整理为csv文件
每个文件名包含采集的时间
文件的内容：
dis arp
                Type: S-Static    D-Dynamic
IP Address       MAC Address     VLAN ID  Interface              Aging Type
10.155.87.54     a85a-f302-54c3  268      GE1/0/1                20    D
10.155.88.87     4031-3c0a-755a  268      GE1/0/1                12    D
先筛选出列数为6的行，
删除vlan列
再将日期加入到接口后面
取列表的前4列


"""
import os
import csv
from datetime import datetime


def walk_dir(file_dir):
    """
    遍历文件夹，返回每个文件的路径
    :param file_dir:
    :return:
    """
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


def archive_ip(dir_path, dst_csv):
    line_list = []
    count = 0
    for file_path in walk_dir(dir_path):
        count += 1
        # 文件名包含手机mac地址的时间
        file_time = os.path.basename(file_path).split('_')[1]
        # 采集时间
        file_date_obj = datetime.strptime(file_time, '%Y%m%d%H%M%S')

        print(count, file_time, len(line_list))
        # 打开每一个文件
        with open(file_path) as fp:
            for line in fp:
                new_line_text = line.split()
                if len(new_line_text) == 6:
                    # print(new_line)
                    # 删除vlan列
                    del new_line_text[2]
                    # 将采集时间插入到接口的后面
                    new_line_text.insert(3, file_date_obj)

                    # if new_line_text[:4] not in line_list:
                    line_list.append(new_line_text[:4])

    with open(dst_csv, 'w', newline='') as fp:
        csv_write = csv.writer(fp)
        csv_write.writerows(line_list)


if __name__ == '__main__':
    # file_name = '10.155.88.254_20220624110506_arp.log'
    # 要导入的文件夹
    dir_path = r'D:\睿智\国土局\政务网\10.155.88.254_arp\202208'
    dst_csv = r'd:\ip_arp_202208.csv'
    if os.path.isdir(dir_path):
        archive_ip(dir_path, dst_csv)
