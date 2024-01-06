# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-20 13:01
"""
import requests

cookies = {
    '_zcy_log_client_uuid': '4698d3e0-9ec9-11ee-83ca-73eba8f41d45',
    'acw_tc': 'ac11000117030475153995751e005d7bf8d09ce6eea4e85b47436cdaeb3a01',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': '_zcy_log_client_uuid=4698d3e0-9ec9-11ee-83ca-73eba8f41d45; acw_tc=ac11000117030475153995751e005d7bf8d09ce6eea4e85b47436cdaeb3a01',
    'Origin': 'http://www.whggzy.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.whggzy.com/site/category?parentId=66007&childrenCode=PoliciesAndRegulations&utm=site.site-PC-49434.959-pc-websitegroup-navBar-front.4.959cf5b09ef211ee87488b7be0b91415',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

json_data = {
    'pageNo': 1,
    'pageSize': 15,
    'categoryCode': 'GovernmentProcurement',
    '_t': 1703047964000,
}

response = requests.post('http://www.whggzy.com/portal/category', cookies=cookies, headers=headers, json=json_data, verify=False)

print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageNo":1,"pageSize":15,"categoryCode":"GovernmentProcurement","_t":1703047964000}'
#response = requests.post('http://www.whggzy.com/portal/category', cookies=cookies, headers=headers, data=data, verify=False)