# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称   ：autoopenserver.PY
# 开发工具   ：PyCharm
'''
  连接MySQL数据库时自动开启服务器
'''
import subprocess
import pymysql
try:
    db=pymysql.connect('127.0.0.1','root','root','mysql') # 连接MySQL数据库
except Exception as e:
    # 判断异常的名字是否为OperationalError
    if e.__class__.__name__=='OperationalError':
        result=subprocess.call('net start mysql80') # 启动MySQL服务，其中mysql80为服务名（可根据实际修改）
        db = pymysql.connect('127.0.0.1', 'root', 'root', 'mysql')  # 连接MySQL数据库
cursor=db.cursor() # 定义游标对象
cursor.execute('select Host,User from user') # 执行SQL查询语句
db.close() # 关闭数据库连接
data=cursor.fetchall() # 得到查询的数据
print('查询结果如下：')
for i in range(0,len(data)): # 遍历查询到的所有数据
    print(data[i]) # 按行输出查询得到的数据
