# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/5 12:45
"""
import pymysql

conn = pymysql.connect(
    host='192.168.1.207',
    port=3306,
    user='root',
    password='admin',
    db='ziliao',
    charset='utf8'
)
# 创建游标对象
cursor = conn.cursor()
# print(cursor)
# sql = 'show tables;'
# cursor.execute(sql)
#
# result=cursor.fetchall()
# print(result)
# SELECT * FROM `idcard` WHERE `name` LIKE '%血%' LIMIT 0, 1000
# 要删除某个字段包含的字符
del_char = "拒查"
sql = f'select * from idcard where name like "%{del_char}%" limit 0 ,1000'
cursor.execute(sql)

for i in cursor.fetchall():
    idcard, name = i
    new_name = name.replace(del_char, "").strip()
    #new_name = name.strip()
    # print(idcard)
    # print(name,new_name)
    # UPDATE `idcard` SET `name`='李好同' WHERE (`idcard`='370723196212214216') AND (`name`='李好同(血型拒查）') LIMIT 1
    # UPDATE `idcard` SET `name`='赵永明' WHERE (`idcard`='370723195601284213') AND (`name`='赵永明（晕血拒测）') LIMIT 1
    new_sql = f'UPDATE `idcard` SET `name`="{new_name}" WHERE (`idcard`="{idcard}") AND (`name`="{name}") LIMIT 1;'
    print(new_sql)
    cursor.execute(new_sql)
    # print(cursor.fetchall())

conn.commit()
cursor.close()
conn.close()
