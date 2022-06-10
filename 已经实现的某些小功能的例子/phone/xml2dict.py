#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/6 17:15
"""
import xmltodict,json,time,os,csv,sys
import time


def parse_xml(file_path):
    '''
    给定一个文件的路径，返回分析结果的字典
    '''

    phone_deal = {       'PROD_INST_ID':'',
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

    file_modtime = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(os.path.getmtime(file_path)+8*3600))
    try:
        with open(file_path, encoding='gbk') as f:
            mystr = f.read()
    except UnicodeDecodeError:
        '''
        打开文件错误，记录下来。
        '''
        with open('./error.log', 'a', encoding='utf-8') as f1:
            f1.write(time.ctime()+" "+file_path+'\n')
        return
    else:
        xml_dict = xmltodict.parse(mystr)
        try:
            phone_dict = xml_dict['root']['data']['Users']['entity']
        except:
            pass
        else:
            # print(type(phone_dict))
            if not hasattr(phone_dict,"get"):
                phone_dict={}
            file_dict = {}
            for i in phone_deal.keys():
                file_dict[i] = phone_dict.get(i)
            file_dict['mod_time'] = file_modtime

        return file_dict


def save2csvfile(file_path, content):
    with open(file_path, 'a', newline='', encoding='utf-8') as f2:
        csv_write = csv.writer(f2)
        csv_write.writerows(content)


if __name__ == '__main__':
    if len(sys.argv) == 0:
        sys.exit(11)
    count=1
    fileStruct = ("PROD_INST_ID",
                      "CUST_ID",
                      "LATN",
                      "BUSI_NBR",
                      "USER_NAME",
                      "CUST_NAME",
                      "INSTALL_ADDR",
                      "CERTIFICATES_NBR",
                      "mod_time")
    content = []
    csvfile = './187.csv'

    for root, dirs, files in os.walk(r'U:\phone\187'):
        for i in files:
            file_path = os.path.join(root, i)
            print('count={0} :{1}'.format(count, file_path))
            file_parse = parse_xml(file_path)
            if file_parse is None:
                continue
            count = count+1
           # print(file_parse)
            content_row = []
            for j in fileStruct:
                content_row.append(file_parse.get(j))
            print(content_row)
            content.append(content_row)

            if count % 10000 == 0:
                save2csvfile(csvfile, content)
                content = []
    save2csvfile(csvfile, content)