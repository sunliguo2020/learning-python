# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/4 20:52
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

cookies = {
    'lianjia_uuid': 'e8d8f4dc-e1dd-485b-8555-40f852b445a5',
    'lianjia_ssid': '2a64858c-4b8a-4330-a193-1a273802646a',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218ea92933e4663-07c94e1c8255b3-26001a51-1296000-18ea92933e714a%22%2C%22%24device_id%22%3A%2218ea92933e4663-07c94e1c8255b3-26001a51-1296000-18ea92933e714a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D',
    'select_city': '110000',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'lianjia_uuid=e8d8f4dc-e1dd-485b-8555-40f852b445a5; lianjia_ssid=2a64858c-4b8a-4330-a193-1a273802646a; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218ea92933e4663-07c94e1c8255b3-26001a51-1296000-18ea92933e714a%22%2C%22%24device_id%22%3A%2218ea92933e4663-07c94e1c8255b3-26001a51-1296000-18ea92933e714a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; select_city=110000',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'mainAuthMethodName': 'username-password',
    'accountSystem': 'customer',
    'credential': {
        'username': '15689266711',
        'password': 'WQzA8+PRPPq9M+Z0hJPxomrkf0oCUgk0cA+cF8qDt8M8miwbnCsD/8L9WBHhYq/J2cm+8MtAVN2tCOaWC6Qvz5D4zI8SnvtccA/DMB9sVPOvydSAgu7XHa1SNnV3QEuKXyzmy0iVNOn5xlxPKV9KPClVXyh7EKleEZq9sxbHQmo=',
        'encodeVersion': '1',
    },
    'context': {
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'clientSource': 'pc',
        'os': 'Windows',
        'osVersion': '10',
        'registerPosLx': 330.5,
        'registerPosLy': 387.5,
        'registerPosRx': 610.5,
        'registerPosRy': 531.5,
        'clickPosX': 498,
        'clickPosY': 414,
        'screen': '702_722',
        'dataId': 'yYa57ih2ixfiLLa2nMFu32WXFvMumwFHMv6WH5ibrH5v0Ywj9iN6ckzyf/UNTzKQ',
    },
    'loginTicketId': 'mzcPQJhpMTAGoPsQMqdyf2d5A0xoA5NT',
    'version': '2.0',
    'srcId': 'eyJ0Ijoie1wiZGF0YVwiOlwiZmUwOWI4N2UxOWIyNDk3NGI0NTE1MzcwZmE2NDU3ZjRmMDdkZWFiYzUzM2ZlMWU2ZGZiYWY5NDY1YjY5NDRhNDhmMDI5Y2MwYmQ2ZDg4MzJmZGYyODE4OTgzZWZiMGI4ODFmZWQ3OGJiODY4ZTFkNTE4NzUyNzBhZjdkMzQ4NWZlYTVlMDk4MjE4NWQ0OGZkOTY1YmQ0ZGJjNzVkN2U5NGM1OWE3MDIwMWMzZTVlNDA3NmY0YjhiMmRlODNiYjI5ZWM3MjRjYWNjNTFiNzcyMzQxY2UxZTA0MzE4Mzc0MTAwOGY5ZGU3OWMxYzcwYjEwMWVkZTQwOTBmNTIxY2NjMFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZDg1OGNmOFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
    'ticketMaxAge': 604800,
}

response = requests.post('https://clogin.ke.com/authentication/authenticate', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"service":"https://ajax.api.ke.com/login/login/getuserinfo","mainAuthMethodName":"username-password","accountSystem":"customer","credential":{"username":"15689266711","password":"WQzA8+PRPPq9M+Z0hJPxomrkf0oCUgk0cA+cF8qDt8M8miwbnCsD/8L9WBHhYq/J2cm+8MtAVN2tCOaWC6Qvz5D4zI8SnvtccA/DMB9sVPOvydSAgu7XHa1SNnV3QEuKXyzmy0iVNOn5xlxPKV9KPClVXyh7EKleEZq9sxbHQmo=","encodeVersion":"1"},"context":{"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","clientSource":"pc","os":"Windows","osVersion":"10","registerPosLx":330.5,"registerPosLy":387.5,"registerPosRx":610.5,"registerPosRy":531.5,"clickPosX":498,"clickPosY":414,"screen":"702_722","dataId":"yYa57ih2ixfiLLa2nMFu32WXFvMumwFHMv6WH5ibrH5v0Ywj9iN6ckzyf/UNTzKQ"},"loginTicketId":"mzcPQJhpMTAGoPsQMqdyf2d5A0xoA5NT","version":"2.0","srcId":"eyJ0Ijoie1wiZGF0YVwiOlwiZmUwOWI4N2UxOWIyNDk3NGI0NTE1MzcwZmE2NDU3ZjRmMDdkZWFiYzUzM2ZlMWU2ZGZiYWY5NDY1YjY5NDRhNDhmMDI5Y2MwYmQ2ZDg4MzJmZGYyODE4OTgzZWZiMGI4ODFmZWQ3OGJiODY4ZTFkNTE4NzUyNzBhZjdkMzQ4NWZlYTVlMDk4MjE4NWQ0OGZkOTY1YmQ0ZGJjNzVkN2U5NGM1OWE3MDIwMWMzZTVlNDA3NmY0YjhiMmRlODNiYjI5ZWM3MjRjYWNjNTFiNzcyMzQxY2UxZTA0MzE4Mzc0MTAwOGY5ZGU3OWMxYzcwYjEwMWVkZTQwOTBmNTIxY2NjMFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZDg1OGNmOFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==","ticketMaxAge":604800}'
#response = requests.post('https://clogin.ke.com/authentication/authenticate', cookies=cookies, headers=headers, data=data)

print(response.json())