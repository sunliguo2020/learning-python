'''
Created on 2016-4-9

@author: Administrator
'''
import MySQLdb
#from bsddb.test.test_all import charset

#print MySQLdb

conn = MySQLdb.Connect(
                      host= "127.0.0.1",
                      port =  3306,
                      user = 'root',
                      passwd = '',
                      db = 'test',
                      charset = 'utf8'           
                      )
print conn
cursor = conn.cursor()
sql ="select * from `201301`"
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()

print rs

rs = cursor.fetchmany(3)

print rs

rs = cursor.fetchall()

#print rs
#print cursor

print cursor
cursor.close()
conn.close()