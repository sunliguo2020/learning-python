# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/7/12 17:30
从mysql中获取记录
"""
import pymysql
import math




def loop_data_from_mysql(table='',sql = None):
    if sql is None:
        return -1

    conn = pymysql.Connect(host='192.168.1.207',
                           user='root',
                           password='admin',
                           database='ziliao',
                           port=3306)
    cur = conn.cursor()
    # 获取数据库的总行数
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
    sql_count = f'select count(1) from `{table}`;'
    cur.execute(sql_count)
    counts = cur.fetchone()
    # print(counts)
    
<<<<<<< HEAD
=======
=======
    sql = f'select count(1) from `{table}`;'
    cur.execute(sql)
    counts = cur.fetchone()
    # print(counts)
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
    per = math.ceil(counts[0] / 5000) + 1
    # print(per)

    for i in range(0, per):

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
        new_sql = sql + 'limit {i * 5000},5000;'

        cur.execute(new_sql)
        inner_result = cur.fetchone()
        
<<<<<<< HEAD
=======
=======
        sql = f'select `id`,`idcard`,`personid` from `{table}` order by `mod_time` DESC limit {i * 5000},5000 ;'

        cur.execute(sql)
        inner_result = cur.fetchone()
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
        while inner_result:
            yield inner_result
            inner_result = cur.fetchone()
