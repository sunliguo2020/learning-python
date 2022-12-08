# -*- coding: utf-8 -*-
'''
Created on 2016-7-30

@author: sunliguo
'''
import MySQLdb
class Conn2mysql:
    def __init__(self,host="192.168.10.102",db="phone",charset="utf8"):
        self.host =  host
        self.db =db
        self.charset = charset
    def conn(self):
        try :
            conn = MySQLdb.connect(host=self.host,
                            port=3306,
                            user="root",
                            passwd="",
                            db=self.db,
                            charset=self.charset
                            )
            cursor = conn.cursor()
            return cursor
        except Exception,e:
            print "Error %s " % e
            print "connect mysql error"
            return -1
        
if __name__ == "__main__":
    conn2sql = Conn2mysql()
    cur=conn2sql.conn()
    cur.execute("show databases")
    print cur.fetchall()
    