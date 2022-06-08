# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/26 20:06
"""

import pymysql

conn = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    db='sdb',
    charset='utf8'
)

cursor = conn.cursor()


def regist():
    username = input("input your name:")
    password = input("input your password:")
    repeatpwd = input('password agin:')
    if password == repeatpwd:
        # 检测注册的用户名是否重复
        query_sql = "select * from users where uname='%s" % username
        cursor.execute(query_sql)
        query_result = cursor.fetchone()
        if query_result is None:
            print("注册成功！")
            insert_sql = "insert into users (username,pwd,email) values(%s,%s,%s)"
            cursor.execute(insert_sql)
            conn.commit()
        else:
            print("用户名重复，注册失败")

    else:
        print("注册失败，两次密码不一致。")


def login():
    username = input("input your name:")
    password = input("input your password:")
    query_sql = 'select * from users where uanme ="%s" and pwd ="%s"' %(user,password)
    #判断登陆状态
