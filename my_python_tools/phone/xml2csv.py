#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 2016-7-14
处理xml保存到文件（csv格式）或者数据库
中文名的文件有问题
2016-7-28
    添加默认数据表
2018-01-17
    只保留保存到csv的部分
2018-01-22
  删除原先带有的引号，要不然导入mysql有错误
  删除换行符
2018-02-24
添加日志记录功能
2019-11-11
添加保存文件名为第一个参数。sys.argv[1].csv
@author: sunliguo
'''
import xml.dom.minidom
import os
import time
import sys

class xml2csv:
    def __init__(self):
        #xml文件中需要关心的节点
        self.phone_deal = {
                     'PROD_INST_ID':'',
                     'LATN':'',
                     'BUSI_NBR':"",
                     'USER_NAME':'',
                     'CUST_NAME':'',
                     'CUST_ID':'',
                     'INSTALL_ADDR':'',
                     'PROD':'',
                     'BRAND':'',
                     'COMBO':'',
                     'CITY_TYPE':'',   
                     'CUST_TYPE':'',   
                     'STRATE_GROUP':'',   
                     'VIP_LEVEL':'', 
                     'CUST_LEVEL':'',   
                     'USER_STATE':'',
                     'ORG_ID':'',     
                     'CERTIFICATES_NBR':'' 
                     }
    #分析xml文件，先创建临时文件，修改gb2312。根据phone_deal 查找属性，返回一条记录
    def parse(self,path):
        #print "path=",path
        if os.path.isfile(path):
            #文件最后修改时间 考虑linux上的时区问题
            #file_modtime = os.stat(path).st_mtime 
            file_modtime = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(os.path.getmtime(path)+8*3600))
            #print "file_modtime= ",file_modtime,type(file_modtime)
            
            xmlfile = open(path)
            #replace 非法字符的处理 文件原先什么编码还没有判断
            replace_utf8=xmlfile.read().decode('GB2312',"replace").encode('UTF-8').replace('GB2312','UTF-8')
            xmlfile.close()
            #print replace_utf8
        else:
            #print "path %s is not file" % path
            self.save2log("path %s is not file \n" % path)
            replace_utf8=""
            return False   
        #创建临时文件
        with open('./linshi.txt',"w") as a:
            a.write(replace_utf8)
       
        #加上如果不是xml的处理
        try:
            DOMTREE = xml.dom.minidom.parse('./linshi.txt')
            Data = DOMTREE.documentElement
        except:
            #print  "%s xml parser error" % path
            self.save2log("%s xml parser error\n" % path )
            return False
        #查找phone_deal 中的关键字
        for i in self.phone_deal.keys():
            #print "i is %s " % i
            #print self.phone_deal[i]
            try:
                #Data.getElementsByTagName(i) 
                #删除原先带有的引号，换行
                self.phone_deal[i]=Data.getElementsByTagName(i)[0].childNodes[0].data.replace('"',"").replace("\n","")
            except Exception:
                self.phone_deal[i]='NULL'
                #print "Not find %s" % i
        #添加文件最后修改时间
        self.phone_deal["mod_time"]= str(file_modtime)
        #如果没有提取到BUSI_NBR字段，补充该文件的路径
        if self.phone_deal["BUSI_NBR"] =="NULL":
            self.phone_deal["BUSI_NBR"]=path
        #如果没啥问题，就返回phone_deal    
        return self.phone_deal

    def save2file(self,xml_result="",savefile="defaultSavefile.txt"):
        if not xml_result:
            return False
        #记录一行文件的列序
        fileStruct =("PROD_INST_ID",
                     "CUST_ID",
                     "LATN",
                     "BUSI_NBR",
                     "USER_NAME",
                     "CUST_NAME",
                     "INSTALL_ADDR",
                     "CERTIFICATES_NBR",
                     "mod_time")
        #保证首行有文件头
        if (os.path.isfile(savefile) and os.path.getsize(savefile) == 0) or not os.path.exists(savefile):
            with open(savefile,"w") as c:
                c.write(repr(fileStruct).replace("(",'').replace(")","").replace("'","")+'\n')
                #c.write(repr(fileStruct))
        str=[]
        for i in fileStruct:
            str.append(xml_result[i])
        str2=""
        for i in str:
            str2+='"'+i+'"'+","
        write_str=str2[:-1]
        with open(savefile,"a") as b:
            b.write(write_str.encode('utf-8')+'\n')
    #记录日志
    def save2log(self,log):
        with open('log.txt','a+') as f:
            f.write(log)   


if __name__=='__main__':

    parser = xml2csv()

    if len(sys.argv) != 0:
        count=1
        for root,dirs,files in os.walk(sys.argv[1]):
            for j in files:
                print("count=",count,":",root+os.path.sep+j)
                result = parser.parse(root+os.path.sep+j)
                if  result:
                    #parser.save2file(result, "savefile2")
                    parser.save2file(result, sys.argv[1]+".csv")
                count+=1