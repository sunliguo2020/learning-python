# -*- coding: utf-8 -*-
'''
Created on 2016-7-4

@author: Administrator
'''
import MySQLdb
sum=0


#合并后的表名
merge_table="2012_xiuji"

#17地市
city=["滨州","德州","东营","菏泽","济南","济宁","莱芜","聊城","临沂","青岛","日照","泰安","威海","潍坊",
      "烟台","枣庄","淄博"]

host = '127.0.0.1'
user = 'root'
passwd = ''
port = 3306
db='2012_xiuji_detail'
db_list =[]
tb_list =[]

Add_Colum="首次接单人"

dbcon = MySQLdb.connect(host,user,passwd,db,port,charset="utf8")
cur = dbcon.cursor()

  
#sql1='alter table'
#for j in ("01","02","03","04","05","06","07","08","09","10","11","12"):
for j in ("01",):
    for i in city:      
       table="2012年"+i+"固话宽带修机明细"  
       #print table
       sql = "desc "+table+" "+Add_Colum
       #print sql
       cur.execute(sql)
       if cur.fetchall():
           print "Table: ",table,Add_Colum,"列存在"
       else:
           #ALTER TABLE `201301滨州固话宽带修机明细`ADD COLUMN `首次接单人`  varchar(255) NULL AFTER `DEAL_USERNAME`;
           sql2 = "alter table "+table+"  add  "+Add_Colum+"  varchar(255) NULL after DEAL_USERNAME"
           print sql2
           cur.execute(sql2)
           if cur.fetchall():
               print '添加成功'
           #print "bucunzai"
        #cur.execute( sql1+"2013"+j+i+"固话宽带修机明细")
        #cur.execute("select count(*) from "+"2013"+j+i+"固话宽带修机明细")
      # print "2015"+j+i
       # sum += cur.fetchall()[0][0]


cur.close()
dbcon.close()