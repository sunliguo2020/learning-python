import requests
def get_buvid3():
    url = 'https://www.bilibili.com/video/BV17R4y1G7qt?spm_id_from=333.999.0.0'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    #将响应头中的cookie获取即可
    result = response.cookies.get_dict()
    return result['buvid3']
buvid3_value = get_buvid3()
print(buvid3_value)