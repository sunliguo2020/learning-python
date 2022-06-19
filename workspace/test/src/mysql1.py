# -*- coding: utf-8 -*-
'''
Created on 2016-7-3

@author: Administrator
'''
import MySQLdb
import sys
import time

host = '127.0.0.1'
user = 'root'
passwd = ''
port = 3306
db_list =[]
tb_list =[]

dbcon = MySQLdb.connect(host,user,passwd,db='test',port=3306,charset="utf8")
cur = dbcon.cursor()

#列出说有的数据库
def check_db():
    cur.execute("show databases")
    print u'数据库总数:',cur.rowcount

    for db in cur.fetchall():
        db_list.append(db[0])
    #db_list=cur.fetchall()
    #print cur.description #返回结果的列信息
    return db_list
#print check_db()
#获取当前数据中所有的 表
def check_table(db):
    cur.execute('use %s' %db)
    cur.execute('select database()')
    print "当前所在数据库:%s" %cur.fetchall()
    all_table = cur.execute("show tables")
    for tb in cur.fetchall():
        print tb
        tb_list.append(tb[0])
    return tb_list       

#print check_table('2015_month')

#判断并创建表
def create_tables(ck_table):
    while True:
        input_table_name = raw_input("请输入要创建的表名").strip()
        print input_table_name
        if len(input_table_name) == 0 :continue
        if input_table_name not in ck_table:
            print "开始创建表:"
            cur.execute("create table %s(`id` int(11) ,`name` char(20))" %input_table_name)
            return input_table_name
        else:
            print "表%s 已存在 ，请再想个新表名" %input_table_name
            time.sleep(1)
        
        
#create_tables(check_table('2015_month'))        
        
        
# sql = "show tables"
# cur.execute(sql)
# print cur.fetchall()
# print cur.rowcount 
# sql2 = 'select * from 201501_sd_xiuji limit 10'      
        
# cur.execute(sql2)
# print cur.fetchone()
# print cur.fetchone()
# print cur.fetchmany(2)
# print cur.rowcount         
#         
#print check_db()
check_table('test')