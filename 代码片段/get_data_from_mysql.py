# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/12 17:30
从mysql中获取记录
"""
import pymysql
import math



<<<<<<< HEAD
def get_data_from_mysql(table=''):
=======
def loop_data_from_mysql(table='',sql = None):
    if sql is None:
        return -1
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
    conn = pymysql.Connect(host='192.168.1.207',
                           user='root',
                           password='admin',
                           database='ziliao',
                           port=3306)
    cur = conn.cursor()
    # 获取数据库的总行数
    sql = f'select count(1) from `{table}`;'
    cur.execute(sql)
    counts = cur.fetchone()
    # print(counts)
    per = math.ceil(counts[0] / 5000) + 1
    # print(per)

    for i in range(0, per):
<<<<<<< HEAD
        sql = f'select `id`,`idcard`,`personid` from `{table}` order by `mod_time` DESC limit {i * 5000},5000 ;'
=======
        # sql = f'select `id`,`idcard`,`personid` from `{table}` order by `mod_time` DESC limit {i * 5000},5000 ;'
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
        cur.execute(sql)
        inner_result = cur.fetchone()
        while inner_result:
            yield inner_result
            inner_result = cur.fetchone()
