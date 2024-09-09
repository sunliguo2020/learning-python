# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-08-23 18:35
"""
import json

# 编写一个Python程序，该程序能够读取一个Excel文件，并提取出其中所有的单元格。
# https://mobile.yangkeduo.com/login.html?from=https%3A%2F%2Fmobile.yangkeduo.com%2Forders.html&refer_page_name=my_order&refer_page_id=10032_1724406738278_r7ftn1wyp1&refer_page_sn=10032
login_url = "https://mobile.yangkeduo.com/login.html"
# 全部订单
total_order_url = "https://mobile.yangkeduo.com/orders.html?type=0&comment_tab=1&combine_orders=1&main_orders=1&refer_page_name=personal&refer_page_id=10001_1724409662228_a14cydbnsw&refer_page_sn=10001"

import requests

cookies = {
    'api_uid': 'CkygjGVsK5Ew4QBoUNxiAg==',
    '_nano_fp': 'XpmoXpdJnqCylpdjXC_2bzU_KVSemyuRbGDGubvG',
    'jrpl': 'S4pmjpqYq4GzCNHdOZaR8elHI5pcsVRr',
    'njrpl': 'S4pmjpqYq4GzCNHdOZaR8elHI5pcsVRr',
    'dilx': 'NCMDwDO5yjSaHl6BNP104',
    'webp': '1',
    'JSESSIONID': '9F74A6BE82D804B836F6432FA3CF140C',
    'PDDAccessToken': 'T4LCUPXWMFBJASZWCR45XN2D2XZSA7G46XMCSLSJTY6KHZXOFQPQ1209d00',
    'pdd_user_id': '7774435485',
    'pdd_user_uin': 'LAWUG3XPPHZCTHIN4MPBTT6IIE_GEXDA',
    'rec_list_personal': 'rec_list_personal_hadkrg',
    'pdd_vds': 'gaLLNOiiGGtytaGEoaLOmaoNEQEIbGPbPanPQaPOaIbyyoPoIyLGbObPEnEy',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'api_uid=CkygjGVsK5Ew4QBoUNxiAg==; _nano_fp=XpmoXpdJnqCylpdjXC_2bzU_KVSemyuRbGDGubvG; jrpl=S4pmjpqYq4GzCNHdOZaR8elHI5pcsVRr; njrpl=S4pmjpqYq4GzCNHdOZaR8elHI5pcsVRr; dilx=NCMDwDO5yjSaHl6BNP104; webp=1; JSESSIONID=9F74A6BE82D804B836F6432FA3CF140C; PDDAccessToken=T4LCUPXWMFBJASZWCR45XN2D2XZSA7G46XMCSLSJTY6KHZXOFQPQ1209d00; pdd_user_id=7774435485; pdd_user_uin=LAWUG3XPPHZCTHIN4MPBTT6IIE_GEXDA; rec_list_personal=rec_list_personal_hadkrg; pdd_vds=gaLLNOiiGGtytaGEoaLOmaoNEQEIbGPbPanPQaPOaIbyyoPoIyLGbObPEnEy',
    'origin': 'https://mobile.yangkeduo.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://mobile.yangkeduo.com/orders.html?type=0&comment_tab=1&combine_orders=1&main_orders=1&refer_page_name=personal&refer_page_id=10001_1724409662228_a14cydbnsw&refer_page_sn=10001',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
}

params = {
    'pdduid': '7774435485',
}

json_data = {
    'type': 'all',
    # 'page': 1,
    'origin_host_name': 'mobile.yangkeduo.com',
    # 'page_from': 0,
    'anti_content': '0asWfqnFmjoyy9exMnGECKEO42hT5F4CNdSUj9O7KG-ZH5fTrRq7ECjjmSBARCDd1hH2XH9a9VmPaO048P4_Va7vgu7_ViuvsvMZnrZjCnrSSA36jz1czdn7qHdh5LIRrHl2te3ypd58eqFuLgA4IDGX5z-1vjH-UROkvsNbJD0BWsjv5QOM3utvyLpQNgBXgd3cpHfgpMd9MvFbeVwo85ab4U_q8ZiHZpNNEJjeMEH1hu3mZuDGUpmrdSJdGu0KA6jlI3-AWQ-xhd0HEuoFtpqz0NhSM8Gu3HSpGuj9rTQtg_s7T7BhN9ynBXAnX42L80Za07a7wT3lp2bTBoAc-YnuF2rOG7r6AyslkywgfG0MzV0o7F1Bn6nUIOk-an8y2gILAzfFBmEJHPitk5eslFdCctdWkgWdJ1f23_ofeQi6uGF_4Fl6bAYC2IR_l_FIYo_GlQIWm_HWGQIh5Lg-VyiRR8nJFxMxRsRnm40XYZRfQDB4rIkRC3r3kQqRoMJSqAC6MTK5KeUpOla-Uvt9bB5gvn5BPq0QV3U64XWUjgNTSyO1eZsEyeZ6hgbbP6N8H1K_z0zEjGxoZPIMgEw_',
    # 'size': 10,
    'offset': 'MO-01-240721-266443231432205',
}

response = requests.post(
    'https://mobile.yangkeduo.com/proxy/api/api/aristotle/order_list_v4',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
# print(response.content)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"type":"all","page":1,"origin_host_name":"mobile.yangkeduo.com","page_from":0,"anti_content":"0asWfqnFmjoyy9exMnGECKEO42hT5F4CNdSUj9O7KG-ZH5fTrRq7ECjjmSBARCDd1hH2XH9a9VmPaO048P4_Va7vgu7_ViuvsvMZnrZjCnrSSA36jz1czdn7qHdh5LIRrHl2te3ypd58eqFuLgA4IDGX5z-1vjH-UROkvsNbJD0BWsjv5QOM3utvyLpQNgBXgd3cpHfgpMd9MvFbeVwo85ab4U_q8ZiHZpNNEJjeMEH1hu3mZuDGUpmrdSJdGu0KA6jlI3-AWQ-xhd0HEuoFtpqz0NhSM8Gu3HSpGuj9rTQtg_s7T7BhN9ynBXAnX42L80Za07a7wT3lp2bTBoAc-YnuF2rOG7r6AyslkywgfG0MzV0o7F1Bn6nUIOk-an8y2gILAzfFBmEJHPitk5eslFdCctdWkgWdJ1f23_ofeQi6uGF_4Fl6bAYC2IR_l_FIYo_GlQIWm_HWGQIh5Lg-VyiRR8nJFxMxRsRnm40XYZRfQDB4rIkRC3r3kQqRoMJSqAC6MTK5KeUpOla-Uvt9bB5gvn5BPq0QV3U64XWUjgNTSyO1eZsEyeZ6hgbbP6N8H1K_z0zEjGxoZPIMgEw_","size":10,"offset":"MO-01-240721-266443231432205"}'
# response = requests.post(
#    'https://mobile.yangkeduo.com/proxy/api/api/aristotle/order_list_v4',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
if __name__ == '__main__':
    for i in range(1, 1000):
        json_data['page'] = i
        json_data['page_from'] = (i-1)*10
        print(json_data['page'], json_data['page_from'])
        response = requests.post(
            'https://mobile.yangkeduo.com/proxy/api/api/aristotle/order_list_v4',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        with open(f"{i}.json", 'w') as fp:
            fp.write(json.dumps(response.json(), ensure_ascii=False))
