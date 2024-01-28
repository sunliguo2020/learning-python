# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/28 15:06
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests
import subprocess

cookies = {
    'ua_id': '3x1gAfVz783ZQGGBAAAAADO0MKdKSnJBu5rOHuiQ9XM=',
    'wxuin': '56237807444586',
    'ptcz': 'e0e5c5f6b0910774a9b8ad14c47d690399a44a0ce54ec66c289de4304fd2c0aa',
    'RK': 'kCUBnUnscA',
    'qq_domain_video_guid_verify': 'a0c595c28dfdbe71',
    '_qimei_uuid42': '1811c0e061b1007eaa50dedd5c3cc9169b5d0c269e',
    'pgv_pvid': '9793031973',
    '_qimei_fingerprint': '582b6b88f4b3c91cdfad58a9c07cc91b',
    '_qimei_q36': '',
    '_qimei_h38': '6add81feaa50dedd5c3cc9160200000b91811c',
    '_clck': '83bx43|1|fis|0',
    'uuid': '82c6bf3e2ef51bdbb002c24d098592ca',
    'cert': 'Qi4Dg4dSYaEyT1izpc4dI8Jem_tKq2mw',
}

headers = {
    'authority': 'mp.weixin.qq.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'ua_id=3x1gAfVz783ZQGGBAAAAADO0MKdKSnJBu5rOHuiQ9XM=; wxuin=56237807444586; ptcz=e0e5c5f6b0910774a9b8ad14c47d690399a44a0ce54ec66c289de4304fd2c0aa; RK=kCUBnUnscA; qq_domain_video_guid_verify=a0c595c28dfdbe71; _qimei_uuid42=1811c0e061b1007eaa50dedd5c3cc9169b5d0c269e; pgv_pvid=9793031973; _qimei_fingerprint=582b6b88f4b3c91cdfad58a9c07cc91b; _qimei_q36=; _qimei_h38=6add81feaa50dedd5c3cc9160200000b91811c; _clck=83bx43|1|fis|0; uuid=82c6bf3e2ef51bdbb002c24d098592ca; cert=Qi4Dg4dSYaEyT1izpc4dI8Jem_tKq2mw',
    'origin': 'https://mp.weixin.qq.com',
    'pragma': 'no-cache',
    'referer': 'https://mp.weixin.qq.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'startlogin',
}
# pwd: v(a.pwd.substr(0, 16)),
res = subprocess.check_output('node v1.js "root"', shell=True)
pwd = res.decode('utf-8')
pwd = pwd.strip()

data = {
    'username': 'sunliguo',
    'pwd': pwd,
    'imgcode': '',
    'f': 'json',
    'userlang': 'zh_CN',
    'redirect_url': '',
    'token': '',
    'lang': 'zh_CN',
    'ajax': '1',
}

response = requests.post('https://mp.weixin.qq.com/cgi-bin/bizlogin',
                         params=params,
                         cookies=cookies,
                         headers=headers,
                         data=data)
print(response.text)
