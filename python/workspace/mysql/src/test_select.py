#-*-coding=utf-8-*-
'''
Created on 2016-4-9

@author: Administrator
'''
import MySQLdb
default_encoding = 'utf-8'

#print MySQLdb

conn = MySQLdb.Connect(
                      host= "127.0.0.1",
                      port =  3306,
                      user = 'root',
                      passwd = '',
                      db = '2013_xiuji_detail',
                      charset = 'utf8'           
                      )
#print conn
cursor = conn.cursor()

#sql = "select count(*) from `201301_xiuji"
sql = 'show tables like "%2013%";'
cursor.execute(sql)

sql2 = """insert into xiuji (  `Textbox41` ,  `LATN_NAME` ,  `SUB_AREA_NAME` ,  `DEAL_ORGIDNAME` ,
  `DEAL_USERNAME` ,
  `首次接单人`,
  `BUSI_NBR` ,
  `SITE_CD` ,
  `SITE_NAME` ,
  `TASK_ORDER_CD` ,
  `INSTALL_ADDR` ,
  `SOURCE_SEND_ORGNAME` ,
  `LAUNCH_NAME` ,
  `SEND_ORGNAME`,
  `CREATE_DT` ,
  `CALL_BACK_DT` ,
  `BACK_DT` ,
  `ARCH_DT` ,
  `BACK_LENGTH2` ,
  `BACK_INTIME_FLAGG_JN` ,
  `BACKCALL_LENGTH2` ,
  `GONGKE_LENGTH2` ,
  `LINK_PHONENO` ,
  `SATISFIED_NAME` ,
  `BACK_COUCITY_INTIME` ,
  `REP_ROCE_TIMES` ,
  `REP_ROCE_TIMEES` ,
  `CUST_HURRY_TIMES` ,
  `CUST_HURRY_TIMEES` ,
  `Textbox56` ,
  `ASK_AGAIN_TIMES` ,
  `ASK_AGAIN_TIMEES` ,
  `CABLE_FLAG` ,
  `CALL_TYPE_NAME2` ,
  `ACCESS_TYPE2` ,
  `PROD_NAME_NAME` ,
  `CITY_TYPE_NAME2` ,
  `CUST_NAME` ,
  `LINK_PHONENO1` ,
  `CALL_NBR` ,
  `REASON_NAME` ,
  `PHENOM_NAME` ,
  `PHENOM_DETAIL` ,
  `LINK_MAN` ,
  `UNSATISFIED_DETAIL2` ,
  `CONTENT`,
  `LAST_URGE_TIME`
) select 
  `Textbox41` ,
  `LATN_NAME` ,
  `SUB_AREA_NAME` ,
  `DEAL_ORGIDNAME` ,
  `DEAL_USERNAME` ,
  `首次接单人`,
  `BUSI_NBR` ,
  `SITE_CD` ,
  `SITE_NAME` ,
  `TASK_ORDER_CD` ,
  `INSTALL_ADDR` ,
  `SOURCE_SEND_ORGNAME` ,
  `LAUNCH_NAME` ,
  `SEND_ORGNAME`,
  `CREATE_DT` ,
  `CALL_BACK_DT` ,
  `BACK_DT` ,
  `ARCH_DT` ,
  `BACK_LENGTH2` ,
  `BACK_INTIME_FLAGG_JN` ,
  `BACKCALL_LENGTH2` ,
  `GONGKE_LENGTH2` ,
  `LINK_PHONENO` ,
  `SATISFIED_NAME` ,
  `BACK_COUCITY_INTIME` ,
  `REP_ROCE_TIMES` ,
  `REP_ROCE_TIMEES` ,
  `CUST_HURRY_TIMES` ,
  `CUST_HURRY_TIMEES` ,
  `Textbox56` ,
  `ASK_AGAIN_TIMES` ,
  `ASK_AGAIN_TIMEES` ,
  `CABLE_FLAG` ,
  `CALL_TYPE_NAME2` ,
  `ACCESS_TYPE2` ,
  `PROD_NAME_NAME` ,
  `CITY_TYPE_NAME2` ,
  `CUST_NAME` ,
  `LINK_PHONENO1` ,
  `CALL_NBR` ,
  `REASON_NAME` ,
  `PHENOM_NAME` ,
  `PHENOM_DETAIL` ,
  `LINK_MAN` ,
  `UNSATISFIED_DETAIL2` ,
  `CONTENT`,
  `LAST_URGE_TIME`
from """

#s= sql4+"201312潍坊固话宽带修机明细;"
#print s
#cursor.execute(s)
rs  = cursor.fetchall()
i=0
for row in rs :
    #s= "%s" %row
    print  row[0]
    #s= sql4+row[0].encode('utf-8')+";"

    
   # sql = sql4+ "%s " % row[0]
    #print sql
    cursor.execute(u"""insert into xiuji (  `Textbox41` ,  `LATN_NAME` ,  `SUB_AREA_NAME` ,  `DEAL_ORGIDNAME` ,
  `DEAL_USERNAME` ,
  `BUSI_NBR` ,
  `SITE_CD` ,
  `SITE_NAME` ,
  `TASK_ORDER_CD` ,
  `INSTALL_ADDR` ,
  `SOURCE_SEND_ORGNAME` ,
  `LAUNCH_NAME` ,
  `CREATE_DT` ,
  `CALL_BACK_DT` ,
  `BACK_DT` ,
  `ARCH_DT` ,
  `BACK_LENGTH2` ,
  `BACK_INTIME_FLAGG_JN` ,
  `BACKCALL_LENGTH2` ,
  `GONGKE_LENGTH2` ,
  `LINK_PHONENO` ,
  `SATISFIED_NAME` ,
  `BACK_COUCITY_INTIME` ,
  `REP_ROCE_TIMES` ,
  `REP_ROCE_TIMEES` ,
  `CUST_HURRY_TIMES` ,
  `CUST_HURRY_TIMEES` ,
  `Textbox56` ,
  `ASK_AGAIN_TIMES` ,
  `ASK_AGAIN_TIMEES` ,
  `CABLE_FLAG` ,
  `CALL_TYPE_NAME2` ,
  `ACCESS_TYPE2` ,
  `PROD_NAME_NAME` ,
  `CITY_TYPE_NAME2` ,
  `CUST_NAME` ,
  `LINK_PHONENO1` ,
  `CALL_NBR` ,
  `REASON_NAME` ,
  `PHENOM_NAME` ,
  `PHENOM_DETAIL` ,
  `LINK_MAN` ,
  `UNSATISFIED_DETAIL2` ,
  `CONTENT`,
  `LAST_URGE_TIME`
) select 
  `Textbox41` ,
  `LATN_NAME` ,
  `SUB_AREA_NAME` ,
  `DEAL_ORGIDNAME` ,
  `DEAL_USERNAME` ,
  `BUSI_NBR` ,
  `SITE_CD` ,
  `SITE_NAME` ,
  `TASK_ORDER_CD` ,
  `INSTALL_ADDR` ,
  `SOURCE_SEND_ORGNAME` ,
  `LAUNCH_NAME` ,
  `CREATE_DT` ,
  `CALL_BACK_DT` ,
  `BACK_DT` ,
  `ARCH_DT` ,
  `BACK_LENGTH2` ,
  `BACK_INTIME_FLAGG_JN` ,
  `BACKCALL_LENGTH2` ,
  `GONGKE_LENGTH2` ,
  `LINK_PHONENO` ,
  `SATISFIED_NAME` ,
  `BACK_COUCITY_INTIME` ,
  `REP_ROCE_TIMES` ,
  `REP_ROCE_TIMEES` ,
  `CUST_HURRY_TIMES` ,
  `CUST_HURRY_TIMEES` ,
  `Textbox56` ,
  `ASK_AGAIN_TIMES` ,
  `ASK_AGAIN_TIMEES` ,
  `CABLE_FLAG` ,
  `CALL_TYPE_NAME2` ,
  `ACCESS_TYPE2` ,
  `PROD_NAME_NAME` ,
  `CITY_TYPE_NAME2` ,
  `CUST_NAME` ,
  `LINK_PHONENO1` ,
  `CALL_NBR` ,
  `REASON_NAME` ,
  `PHENOM_NAME` ,
  `PHENOM_DETAIL` ,
  `LINK_MAN` ,
  `UNSATISFIED_DETAIL2` ,
  `CONTENT`,
  `LAST_URGE_TIME`
from %s""" % row[0])
    i+=1
    #cursor.execute(sql4)
    #print type(sql3)
  
print i


#print cursor
#print cursor
cursor.close()
conn.close()