# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-04 7:54
"""
import requests
from bs4 import BeautifulSoup

cookies = {
    'track_playlist': '[{%22id%22:%22101947%22%2C%22name%22:%225566%20-%20%E5%A5%BD%E4%B9%85%E4%B8%8D%E8%A7%81(Dj%E9%98%BF%E6%B6%9B%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E7%94%B7)%22%2C%22link%22:%22https://www.172mix.com/play/101947.html%22}%2C{%22id%22:%22166885%22%2C%22name%22:%22%E3%80%90172Mix%E7%8B%AC%E5%AE%B6%E3%80%91%E5%BE%90%E4%BD%B3%E8%8E%B9%20-%20%E8%BA%AB%E9%AA%91%E7%99%BD%E9%A9%AC(DjE%E7%A5%9E%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E5%A5%B3)%E6%8A%96%E9%9F%B3%22%2C%22link%22:%22https://www.172mix.com/play/166885.html%22}%2C{%22id%22:%22166884%22%2C%22name%22:%22%E3%80%90172Mix%E7%8B%AC%E5%AE%B6%E3%80%91%E6%9F%AF%E5%8F%97%E8%89%AF%20-%20%E5%A4%A7%E5%93%A5(DjE%E7%A5%9E%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E7%94%B7)%22%2C%22link%22:%22https://www.172mix.com/play/166884.html%22}]',
    'Hm_lvt_b06193fdab4f5036273288a915b554af': '1709509210',
    'Hm_lpvt_b06193fdab4f5036273288a915b554af': '1709509935',
    'XSRF-TOKEN': 'eyJpdiI6IjgrcXhqRG9OcHIwRlZYNk5CbjRCeWc9PSIsInZhbHVlIjoiQnc0MTZUR3MxSEtHV09cL0plV1Y3NkFpU2JJNDd1MnpJYmJCSnpHRUpZQkRodUJIXC9YVUR4Qm9maWEyRmg0dmJ4TzRrQnMyOVZ6Z3g0dmJVeXNaTzFydkJySGVpWkREZXV0ZjA3a04xNE1kQnBZdDh5SWNzRDBiZW5YR1BVN3lTaiIsIm1hYyI6IjFhYWNjMDkzMDc2Yzc5ZjA1Y2VmNjljYzgyNDM5MWI5ZTU2NjIyMzk3NDk5NGJkNTVhZDM4Yzg2M2NlNDcyNGUifQ%3D%3D',
    '172mix_session': 'eyJpdiI6IlpUdURQR2duVEpKZFNVRFMyZTM1WEE9PSIsInZhbHVlIjoiSUVNUXpudzloY0RNRndtQWgxcXM2SE5PQTJVRUhwa0JXcjd1dUVlaXlHRlRJSDRQVnJ6REVoRElnb2RyVkh3K21zOTNLRFVCQ1VYWGplMHE1VWxYOTM2UTBMXC9NM1wvTldhMEppOExmS1ZnR1dFcTlkMFwvVTF0OENFRWd0QU1QTjEiLCJtYWMiOiJmNDE5ODRjNGMxZTc4NmQyMTE3ZjQ1ODM1NDk0MjE4MzE4OTI5ZDIyYmE0ZGJhYzRiM2E4NzAyZjQ2NWExNDUwIn0%3D',
}

headers = {
    'authority': 'www.172mix.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'track_playlist=[{%22id%22:%22101947%22%2C%22name%22:%225566%20-%20%E5%A5%BD%E4%B9%85%E4%B8%8D%E8%A7%81(Dj%E9%98%BF%E6%B6%9B%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E7%94%B7)%22%2C%22link%22:%22https://www.172mix.com/play/101947.html%22}%2C{%22id%22:%22166885%22%2C%22name%22:%22%E3%80%90172Mix%E7%8B%AC%E5%AE%B6%E3%80%91%E5%BE%90%E4%BD%B3%E8%8E%B9%20-%20%E8%BA%AB%E9%AA%91%E7%99%BD%E9%A9%AC(DjE%E7%A5%9E%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E5%A5%B3)%E6%8A%96%E9%9F%B3%22%2C%22link%22:%22https://www.172mix.com/play/166885.html%22}%2C{%22id%22:%22166884%22%2C%22name%22:%22%E3%80%90172Mix%E7%8B%AC%E5%AE%B6%E3%80%91%E6%9F%AF%E5%8F%97%E8%89%AF%20-%20%E5%A4%A7%E5%93%A5(DjE%E7%A5%9E%20Electro%20Mix%E5%9B%BD%E8%AF%AD%E7%94%B7)%22%2C%22link%22:%22https://www.172mix.com/play/166884.html%22}]; Hm_lvt_b06193fdab4f5036273288a915b554af=1709509210; Hm_lpvt_b06193fdab4f5036273288a915b554af=1709509935; XSRF-TOKEN=eyJpdiI6IjgrcXhqRG9OcHIwRlZYNk5CbjRCeWc9PSIsInZhbHVlIjoiQnc0MTZUR3MxSEtHV09cL0plV1Y3NkFpU2JJNDd1MnpJYmJCSnpHRUpZQkRodUJIXC9YVUR4Qm9maWEyRmg0dmJ4TzRrQnMyOVZ6Z3g0dmJVeXNaTzFydkJySGVpWkREZXV0ZjA3a04xNE1kQnBZdDh5SWNzRDBiZW5YR1BVN3lTaiIsIm1hYyI6IjFhYWNjMDkzMDc2Yzc5ZjA1Y2VmNjljYzgyNDM5MWI5ZTU2NjIyMzk3NDk5NGJkNTVhZDM4Yzg2M2NlNDcyNGUifQ%3D%3D; 172mix_session=eyJpdiI6IlpUdURQR2duVEpKZFNVRFMyZTM1WEE9PSIsInZhbHVlIjoiSUVNUXpudzloY0RNRndtQWgxcXM2SE5PQTJVRUhwa0JXcjd1dUVlaXlHRlRJSDRQVnJ6REVoRElnb2RyVkh3K21zOTNLRFVCQ1VYWGplMHE1VWxYOTM2UTBMXC9NM1wvTldhMEppOExmS1ZnR1dFcTlkMFwvVTF0OENFRWd0QU1QTjEiLCJtYWMiOiJmNDE5ODRjNGMxZTc4NmQyMTE3ZjQ1ODM1NDk0MjE4MzE4OTI5ZDIyYmE0ZGJhYzRiM2E4NzAyZjQ2NWExNDUwIn0%3D',
    'pragma': 'no-cache',
    'referer': 'https://www.172mix.com/play/166885.html',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
}

response = requests.get('https://www.172mix.com/play/101947.html', cookies=cookies, headers=headers)

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 获取视频链接
# video_link = soup.find('video')['src']
# print(response.text)
