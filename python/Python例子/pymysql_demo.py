# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/28 15:14
"""
import pymysql

conn = pymysql.Connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='',
                       db='ziliao',
                       charset='utf8')
cur = conn.cursor()
sql = 'show tables;'
cur.execute(sql)
print(cur.rowcount)
print(cur.fetchone())
print(cur.fetchall())
cur.close()
conn.commit()
conn.close()
