# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/30 11:27
"""
import  requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

params = {
    "cname":"",
        "pid":"",
"keyword": "北京",
"pageIndex": "1",
"pageSize": "10"
}
response = requests.post(url=url,data=params)

page_text = response.json()
print(page_text
      )
for dic in page_text['Table1']:
   print(dic['storeName'],dic['addressDetail'])
