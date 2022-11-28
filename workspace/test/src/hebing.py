# -*- coding: utf-8 -*-
'''
Created on 2016-6-1

@author: Administrator
'''
import MySQLdb
sum=0


#合并后的表名
merge_table="2012_2015_xiuji"

#17地市
city=["滨州","德州","东营","菏泽","济南","济宁","莱芜","聊城","临沂","青岛","日照","泰安","威海","潍坊",
      "烟台","枣庄","淄博"]

host = '127.0.0.1'
user = 'root'
passwd = ''
port = 3306
db="2012_xiuji_detail"
db_list =[]
tb_list =[]

dbcon = MySQLdb.connect(host,user,passwd,db,port=3306,charset="utf8")
cur = dbcon.cursor()

def get_tables(db):
    cur.execute('use %s' %db)
    cur.execute('select database()')
    print "当前所在数据库:%s" %cur.fetchall()
    all_table = cur.execute("show tables")
    for tb in cur.fetchall():
        tb_list.append(tb[0])
        #print tb[0]
    return tb_list

value='''
   `Textbox41`,
  `LATN_NAME`,
  `SUB_AREA_NAME`,
  `DEAL_ORGIDNAME`,
  `DEAL_USERNAME`,
  `首次接单人`,
  `BUSI_NBR`,
  `SITE_CD`,
  `SITE_NAME`,
  `TASK_ORDER_CD`,
  `INSTALL_ADDR`,
  `SOURCE_SEND_ORGNAME`,
  `LAUNCH_NAME`,
  `SEND_ORGNAME`,
  `CREATE_DT`,
  `CALL_BACK_DT`,
  `BACK_DT`,
  `ARCH_DT`,
  `BACK_LENGTH2`,
  `BACK_INTIME_FLAGG_JN`,
  `BACKCALL_LENGTH2`,
  `GONGKE_LENGTH2`,
  `LINK_PHONENO`,
  `SATISFIED_NAME`,
  `BACK_COUCITY_INTIME`,
  `REP_ROCE_TIMES`,
  `REP_ROCE_TIMEES`,
  `CUST_HURRY_TIMES`,
  `CUST_HURRY_TIMEES`,
  `Textbox56`,
  `ASK_AGAIN_TIMES`,
  `ASK_AGAIN_TIMEES`,
  `CABLE_FLAG`,
  `CALL_TYPE_NAME2`,
  `ACCESS_TYPE2`,
  `PROD_NAME_NAME`,
  `CITY_TYPE_NAME2`,
  `CUST_NAME`,
  `LINK_MAN`,
  `LINK_PHONENO1`,
  `CALL_NBR`,
  `REASON_NAME`,
  `PHENOM_NAME`,
  `PHENOM_DETAIL`,
  `UNSATISFIED_DETAIL2`,
  `CONTENT`
'''
sql1='insert into '+ merge_table+'('+value+' ) select '+value+'from '
'''
#for j in ("01","02","03","04","05","06","07","08","09","10","11","12"):
for j in ("01",):
    for i in city:      
        table="2012年"+i+"固话宽带修机明细"  
        print table
        cur.execute( sql1+table)
        cur.execute("select count(*) from "+table)
        sum += cur.fetchall()[0][0]            
print "sum",sum
'''
'''
cur.execute("show tables")
for tb_list in cur.fetchall():    
    #print tb_list[0]
    cur.execute("select count(*) from "+tb_list[0])
    sum += cur.fetchall()[0][0]
print "All tables's lines is ",sum
'''

Alltables=get_tables("year_xiuji_detail")
# cur.execute("show tables")
# for i in  cur.fetchall():
#     print i
for i in Alltables:
    #print sql1+Alltables[0].encode('utf-8')
    print i
    cur.execute(sql1+i.encode('utf-8'))
cur.close()
dbcon.close()