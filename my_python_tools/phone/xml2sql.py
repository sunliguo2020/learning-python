#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-7-30

@author: sunliguo
'''
#import Xml2csv
from Xml2csv import Xml2csv
from Xml2csv import Conn2mysql
import sys,os

parser = Xml2csv()

conn2sql =Conn2mysql()
cur=conn2sql.conn()
if  cur != None:
    cur.execute("select database()") 
    print "当前所在数据库:%s" %cur.fetchall() 
else:
    print "connect to mysql error"
    exit(-1)
if len(sys.argv) == 3:
    
    count=1
    for root,dictorys,files in os.walk(sys.argv[1]):
        for j in files:
            #print "root = ",root
            #print "files = ",j
            print "count=",count,":",root+os.path.sep+j
            result = parser.parse(root+os.path.sep+j)
            if  result:
                    #print type(result['USER_NAME'])
                parser.save2mysql(cur,result,sys.argv[2])
                    #cursor.execute("insert into xml2sql values(1,'2',3,4,5,6,7,8,9)")
                    #print cursor.fetchall()
            count+=1
else:
    print "usage %s directory_path sql_table" % sys.argv[0]