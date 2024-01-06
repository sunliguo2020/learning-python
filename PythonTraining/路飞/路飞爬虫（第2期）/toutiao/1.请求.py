# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-24 10:05
"""
import requests

url = 'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398968&max_behot_time=1703374408&offset=0&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web'

resp = requests.get(url)
print(resp.text)
