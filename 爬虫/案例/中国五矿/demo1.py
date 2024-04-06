# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/4 8:01
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""

import requests

cookies = {
    'SUNWAY-ESCM-COOKIE': '3506dd53-eefb-4c29-8d44-3988b8ebf5c5',
    '__jsluid_s': 'e8ccb587398d5dd4deed542e996fe6c8',
    'JSESSIONID': 'D6ECD7ED767451147D5D31820514C512',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'SUNWAY-ESCM-COOKIE=3506dd53-eefb-4c29-8d44-3988b8ebf5c5; __jsluid_s=e8ccb587398d5dd4deed542e996fe6c8; JSESSIONID=D6ECD7ED767451147D5D31820514C512',
    'Origin': 'https://ec.minmetals.com.cn',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'param': 'b4SoaQrd9C/cUZZAfH//iw3iofSNBc5t3A+i9xk7gWyTQOnJJD1ve+cU1bP1fK7Zgfl27xlVydpmQEMqHjOls/vVL/XbWih97PmM4Cs046u2EAVYRedZZwz8gLeyPtkhjjMTzU6DDgKsW2A3PWwrcNVxwUkhIBuLnoIm8pIuLDUm49Epu4y/O1L+0VqyuPI6HR7sF8q89MX0W2QszAQ7xRDDjJXhnZ+YGIKT6Yx9JtdgGZ9t9/KvRJNK9ig9Q6Zs4jOdSPTxxh8WtHH9z9qTsJ9W/JNhBCMxhGpJDyZXVGgNo3em50NxxYtYtgi24kpipvJszNeYeVc5wIM9R/i9IVKDsG50P+lkHk/8EV3yNaZWnjKFBPweBTNDhgEZsVHfdi3kMImfOYjyk9HF60g4+0KaOpQmGHs/tJQRhYnE2GGuWucCyeNa+Fanpa/qTfwHAFY8alJIz9CZGSnNSNvpFC+0XX9dthZCeE1lTGYJxH7m6WvtpKvvsBgoQqYZPYioN1kjl0AAaiSEgzB8gYrZjjptBDMyiRvHoGBZ9Sz1nCasdham0gj0f8ZcZRAL5W9gOuX/W0L10RU9gtgYsBshAOcjrSzdtV8agxR9MRM00pZq2McdPuPGvmOap7o0PppgPZv/LFlRDPfFpE1PDECV5LJ0oBNFJ9nd4GPKntZqOVw=',
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"param":"b4SoaQrd9C/cUZZAfH//iw3iofSNBc5t3A+i9xk7gWyTQOnJJD1ve+cU1bP1fK7Zgfl27xlVydpmQEMqHjOls/vVL/XbWih97PmM4Cs046u2EAVYRedZZwz8gLeyPtkhjjMTzU6DDgKsW2A3PWwrcNVxwUkhIBuLnoIm8pIuLDUm49Epu4y/O1L+0VqyuPI6HR7sF8q89MX0W2QszAQ7xRDDjJXhnZ+YGIKT6Yx9JtdgGZ9t9/KvRJNK9ig9Q6Zs4jOdSPTxxh8WtHH9z9qTsJ9W/JNhBCMxhGpJDyZXVGgNo3em50NxxYtYtgi24kpipvJszNeYeVc5wIM9R/i9IVKDsG50P+lkHk/8EV3yNaZWnjKFBPweBTNDhgEZsVHfdi3kMImfOYjyk9HF60g4+0KaOpQmGHs/tJQRhYnE2GGuWucCyeNa+Fanpa/qTfwHAFY8alJIz9CZGSnNSNvpFC+0XX9dthZCeE1lTGYJxH7m6WvtpKvvsBgoQqYZPYioN1kjl0AAaiSEgzB8gYrZjjptBDMyiRvHoGBZ9Sz1nCasdham0gj0f8ZcZRAL5W9gOuX/W0L10RU9gtgYsBshAOcjrSzdtV8agxR9MRM00pZq2McdPuPGvmOap7o0PppgPZv/LFlRDPfFpE1PDECV5LJ0oBNFJ9nd4GPKntZqOVw="}'
#response = requests.post('https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page', cookies=cookies, headers=headers, data=data)

print(response.json())