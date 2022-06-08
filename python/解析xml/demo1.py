# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/9 7:00
"""
from lxml import etree
import os


def parse_xml(xml):
    data_index = ['PROD_INST_ID', 'CUST_ID', 'LATN', 'BUSI_NBR', 'USER_NAME', 'CUST_NAME', 'INSTALL_ADDR','CERTIFICATES_NBR']
    data_dict = {
                "PROD_INST_ID": '',
                 "CUST_ID": '',
                 "LATN": '',
                 "BUSI_NBR": '',
                 "USER_NAME": '',
                 "CUST_NAME": '',
                 "INSTALL_ADDR": '',
                 "CERTIFICATES_NBR": ''

                 }
    parser = etree.XMLParser(encoding='utf-8')
    users_xml = etree.parse(xml)
    # # print(type(users_xml))
    # BUSI_NBR = users_xml.xpath('//BUSI_NBR/text()')[0]
    # PROD_INST_ID = users_xml.xpath('//PROD_INST_ID/text()')[0]
    # print(BUSI_NBR)
    for k in data_index:
        result = users_xml.xpath(f'//{k}/text()')
        if result:
            data_dict[k] = result[0]
        else:
            data_dict[k] =''
    # for k,v in data_dict.items():
    #     print(k,v)

    return data_dict

if __name__ == '__main__':

    for root,dirs,files in os.walk('../../mysql_blob/phone'):
        for file in files:
            file_path  = os.path.join(root,file)
            # with open(file_path,'r',encoding='gbk') as fp:

            print(parse_xml(file_path))
