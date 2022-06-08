# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/18 14:49
"""
import json
import os

import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017')
#
# dblist = myclient.list_databases()
# for i in dblist:
#     print(i)

conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
# 切换数据库/集合
sgy = conn['sgy']

root_dir = r'd:\pycharm\ShouGuangYun\jiankang\hisSummary'

for root, dirs, files in os.walk(root_dir):
    for f in files:
        file_path = os.path.join(root, f)
        print(file_path)
        with open(file_path) as fp:
            file_con = fp.read()
            if file_con:
                print(file_con)
                try:
                    json_data = json.loads(file_con)
                    sgy['hissummary'].insert_one({"file_name": f, "file_data": json_data})
                except Exception as e:
                    print("插入失败", e)
