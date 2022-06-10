# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/7 19:14
把手机L6导出的短信整理为csv形式

"""
import csv
import os

import chardet

csv_list = []
FILE_PATH = r'U:\sunliguo\我的手机\L6\short_message'

for root, dirs, files in os.walk(FILE_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        # print(file_path)

        # 检测文件的编码
        with open(file_path, 'rb') as fp:
            content = fp.read()
        file_encoding = chardet.detect(content)['encoding']
        # print(file_encoding)

        # with open(file_path,encoding='utf-16-le') as fp:
        with open(file_path, encoding=file_encoding) as fp:
            content = fp.readlines()

            # 删除每行末尾的 \n
            # for i in content:
            #     i.replace('\n','')
            for i in range(0, len(content)):
                content[i] = content[i].replace("\n", "")
            print(content)
            csv_list.append(content)

with open('shortmessage.csv', 'w', encoding='utf-8', newline='') as fp:
    csv_write = csv.writer(fp)
    csv_write.writerows(csv_list)
