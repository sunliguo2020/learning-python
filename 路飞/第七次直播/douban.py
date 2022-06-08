# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/1/30 10:41
"""
import requests
parms = {"type":"13",
         "interval_id":"100:90",
         "action":"",
         "start":"0",
         "limit":"20"}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = "https://movie.douban.com/j/chart/top_list"
response  = requests.get(url=url,headers=headers,params=parms)
page_text = response.json()
fp = open('douban.txt','w',encoding='utf-8')
for dic in page_text:
    title = dic['title']
    score = dic['score']
    fp.write(title+score+'\n')
fp.close()

#print(dir(response))
