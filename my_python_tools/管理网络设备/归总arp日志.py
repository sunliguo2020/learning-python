# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/12 16:28

统计归档国土局政务网所有的arp记录，汇总为csv文件
记录格式：time,ip,mac,port
修改记录：
1、2022-04-12 23:38 csv添加表头
2、2022-04-12 23:51 保存到一个csv文件中
"""
import csv
import datetime
import os

re_b = b'1B5B313644202020202020202020202020202020201B5B313644'
re_a = '[16D'
re_c = b'0x1B5B313644'
# 要替换的
re_d = '[16D                [16D'

rows = [['time', 'ip', 'mac', 'port']]
new_file_name = 'all.csv'
if os.path.isfile(new_file_name):
    os.remove(new_file_name)


for root, dirs, files in os.walk(r'd:\10.155.88.254_arp'):
    for file in files:
        file_path = os.path.join(root, file)

        date_list = file.split('_')
        # 当前文件的日期str格式
        date_str = date_list[1] + '-' + date_list[2] + '-' + date_list[3] + ' ' + date_list[4] + ":" + date_list[
            5] + ":" + date_list[6]
        # 转换为日期格式
        shijian_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

        # result 保存10.155.8X的记录
        result = ''
        print(file_path)
        with open(file_path, 'r') as fp:
            content = fp.read()
        new_content = content.replace(re_d, '')
        for i in new_content.split('\n'):
            # 只统计10.155.8X的ip地址
            if i.startswith('10.155.8'):
                result += i + '\n'

        # 每行开头添加记录的日期和时间，并删除无用的列，保存在rows中

        for i in result.split('\n'):
            row = i.split()
            # 排除空行
            if len(row) > 2:
                row.insert(0, str(shijian_date))
                # 删除无用的列
                del row[-2:]
                del row[-2]

                rows.append(row)

    # 保存新纪录
    with open(new_file_name, 'a', newline='') as fp:
        csv_write = csv.writer(fp, quoting=csv.QUOTE_ALL)
        csv_write.writerows(rows)
        rows = []
