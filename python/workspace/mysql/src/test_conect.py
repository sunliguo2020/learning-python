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
                      db = 'xml',
                      charset = 'utf8'           
                      )
print conn
cusor = conn.cursor()

#print cursor
print cusor
cusor.close()
conn.close()