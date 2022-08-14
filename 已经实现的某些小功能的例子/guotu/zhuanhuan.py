# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/26 10:50
"""
import os
import datetime
import shutil


dir_path = r'D:\睿智\国土局\政务网\10.155.88.254_arp\zhuanhuan'

for root, dirs, files in os.walk(dir_path):
    for file in files:
        # file_path = os.path.join(root, file)
        print(root)
        print(file)
        time_str = file.replace('10.155.88.254_','').replace('_arp.log','')
        # print(time_str)
        date_str = datetime.datetime.strptime(time_str,'%Y_%m_%d_%H_%M_%S')
        date_str_2 = datetime.datetime.strftime(date_str,'%Y%m%d%H%M%S')
        # print(date_str_2)
        new_file_name = '10.155.88.254_'+date_str_2+'_arp.log'
        print(new_file_name)
        shutil.move(os.path.join(root,file),os.path.join(root,new_file_name))
