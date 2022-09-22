# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/1 11:30
"""
import requests
import csv
def getmachineinfobysn(sn):
    url = f'https://newsupport.lenovo.com.cn/api/machine/getmachineinfo?sn={sn}'
    resq = requests.get(url)
    resp_json  = resq.json()
    if resp_json.get('data') != []:
        machineno = resp_json.get('data').get('MachineNo')
        productdate = resp_json.get('data').get('ProductDate')
        productmodel = resp_json.get('data').get('ProductModel')

        csv_line  = [machineno,productmodel,productdate]
        with open('sn_csv2.csv','a',newline=' ') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerow(csv_line)

    # with open(sn+'.txt','w',encoding='utf-8') as fp:
    #     fp.write(str(resq.json()))

if __name__ == '__main__':
    with open('sn.txt',"r") as fp:
        for line in fp:
            line = line.replace('\n','')
            print(line)
            getmachineinfobysn(line)