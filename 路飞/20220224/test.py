# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/24 22:32
"""
import pymysql

#创建连接对象
conn = pymysql.Connect(host="127.0.0.1",
                       port=3306,
                       user='root',
                       password='xxx',
                       db="ziliao",
                       charset='utf8')
#创建游标对象
cursor = conn.cursor()
#执行sql语句
