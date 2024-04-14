# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/13 23:51
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

cookies = {
    'PHPSESSID': 'd5a268964ef6e7b30a6de6c1d91a2ce56e6ccfb5',
    'access_origin': 'https%3A//cn.bing.com/',
    'epweike_zturl': 'https%3A//zt.epwk.com/wk20/%3Fepi%3D1443368%26utm_source%3Dpc-360%26utm_medium%3D%26utm_campaign%3D%26utm_content%3D%26utm_term%3D%25E5%25A8%2581%25E5%25AE%25A2',
    'epweike_zturl_back': 'https%3A//zt.epwk.com/wk20/%3Fepi%3D1443368%26utm_source%3Dpc-360%26utm_medium%3D%26utm_campaign%3D%26utm_content%3D%26utm_term%3D%25E5%25A8%2581%25E5%25AE%25A2',
    'epweike_construction_epi': 'construction_epi',
    'user_prom_event': '1443368',
    'Hm_lvt_387b8f4fdb89d4ea233922bdc6466394': '1713023197',
    'hy_data_2020_id': '18ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d',
    'sajssdk_2020_cross_new_user': '1',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d%22%2C%22site_id%22%3A1314%2C%22user_company%22%3A1280%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22pc-360%22%2C%22%24latest_utm_term%22%3A%22%E5%A8%81%E5%AE%A2%22%7D%2C%22device_id%22%3A%2218ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d%22%7D',
    'Hm_lvt_e6c705a49657dec3d6b1ad798c50243e': '1713023197',
    'Hm_lpvt_e6c705a49657dec3d6b1ad798c50243e': '1713023197',
    'HWWAFSESID': '45ce0732e18238b415',
    'HWWAFSESTIME': '1713023199355',
    'login_referer': 'https%3A%2F%2Fzt.epwk.com%2F',
    'Hm_lpvt_387b8f4fdb89d4ea233922bdc6466394': '1713023199',
    'time_diff': '0',
    'XDEBUG_SESSION': 'XDEBUG_ECLIPSE',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Access-Token': '',
    'App-Id': '4ac490420ac63db4',
    'App-Ver': '',
    'CHOST': 'www.epwk.com',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'PHPSESSID=d5a268964ef6e7b30a6de6c1d91a2ce56e6ccfb5; access_origin=https%3A//cn.bing.com/; epweike_zturl=https%3A//zt.epwk.com/wk20/%3Fepi%3D1443368%26utm_source%3Dpc-360%26utm_medium%3D%26utm_campaign%3D%26utm_content%3D%26utm_term%3D%25E5%25A8%2581%25E5%25AE%25A2; epweike_zturl_back=https%3A//zt.epwk.com/wk20/%3Fepi%3D1443368%26utm_source%3Dpc-360%26utm_medium%3D%26utm_campaign%3D%26utm_content%3D%26utm_term%3D%25E5%25A8%2581%25E5%25AE%25A2; epweike_construction_epi=construction_epi; user_prom_event=1443368; Hm_lvt_387b8f4fdb89d4ea233922bdc6466394=1713023197; hy_data_2020_id=18ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d; sajssdk_2020_cross_new_user=1; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d%22%2C%22site_id%22%3A1314%2C%22user_company%22%3A1280%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22pc-360%22%2C%22%24latest_utm_term%22%3A%22%E5%A8%81%E5%AE%A2%22%7D%2C%22device_id%22%3A%2218ed8239de41d7-0724fa1150a758-26001a51-1296000-18ed8239de559d%22%7D; Hm_lvt_e6c705a49657dec3d6b1ad798c50243e=1713023197; Hm_lpvt_e6c705a49657dec3d6b1ad798c50243e=1713023197; HWWAFSESID=45ce0732e18238b415; HWWAFSESTIME=1713023199355; login_referer=https%3A%2F%2Fzt.epwk.com%2F; Hm_lpvt_387b8f4fdb89d4ea233922bdc6466394=1713023199; time_diff=0; XDEBUG_SESSION=XDEBUG_ECLIPSE',
    'Device-Os': 'web',
    'Device-Ver': '',
    'Imei': '',
    'NonceStr': '1713023223f5827',
    'Origin': 'https://www.epwk.com',
    'Os-Ver': '',
    'Pragma': 'no-cache',
    'Referer': 'https://www.epwk.com/login.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Signature': 'RgsrPe+ievV65rHUztK+RoqlMXOW+LmP9hMNMIFWceHJXUuugAkgW83da7kzrAEf',
    'Timestemp': '1713023223',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-REQUEST-ID': 'b3d8eac16ac9c37a927e7d1405c298fe',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'username': '15689266172',
    'password': '123456',
    'code': '',
    'hdn_refer': 'https://zt.epwk.com/',
}

response = requests.post('https://www.epwk.com/api/epwk/v1/user/login',
                         cookies=cookies,
                         headers=headers,
                         data=data)

print(response.text)