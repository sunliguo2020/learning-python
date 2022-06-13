# -*- coding: utf-8 -*-
'''
 @Time : 2022/6/12 6:07
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : python_repos.py
 @Project : learning-python
'''
import requests
#执行API调用并存储响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept':'applicationg/vnd.githu.v3+json'}
r = requests.get(url,headers  = headers)
print(f"Status code:{r.status_code}")
#将api响应赋值一个变量
response_dict = r.json()
#处理结果
print(response_dict.keys())

