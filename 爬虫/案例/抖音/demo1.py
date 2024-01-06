# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-12-31 10:02
"""
import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'ttwid=1%7Cw4utNfHqnGVEZv22hWTZv2hP_N8Gx5SzH8mXywON7y4%7C1703987774%7Cfb4580a3887a6e2b88d5ca4a3eda20e8353edf6d5bd32cdc6110caf6e7d4ca98; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; dy_swidth=1366; dy_sheight=768; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1366%2C%5C%22screen_height%5C%22%3A768%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; csrf_session_id=84188890b3f5892d371413bd97873b1d; strategyABtestKey=%221703987779.688%22; s_v_web_id=verify_lqsubuki_LySZNanZ_WLgL_4wnj_Bywr_AkARl3EkCxAa; passport_csrf_token=191a5199bbda49e1a4afead6141559eb; passport_csrf_token_default=191a5199bbda49e1a4afead6141559eb; bd_ticket_guard_client_web_domain=2; ttcid=86441bc62c5e4e56acd638b0212d44b026; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; download_guide=%221%2F20231231%2F0%22; pwa2=%220%7C0%7C1%7C0%22; __ac_nonce=06590caa1007cb19b8c83; __ac_signature=_02B4Z6wo00f01BfaTDQAAIDDKnNWq9ZBPjwX-kiAAGBsWSTh7x0r9nc0uT.IxMoHO4pIkjLVoqOo4w83RQyvVE8kJPly35kwX6mqdwperMZe6-3gvgXAP-8GjZqvMjqa.Mll5oAx7.fqrSyze3; SEARCH_RESULT_LIST_TYPE=%22single%22; msToken=zzsRDJAi7Ai3lZiVYmoXX-QTtQak2yfl4FjzypBxpW6nv_aTKOAtCoX7fkeTOQc-5g09xi-HIgDXP0DSp5Uj4QXfV9F4ULPT5blgtViFk0aWQRbkEg==; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSnVaRWk2amF3N0FZSnByMDBDdUg4Rk9NcVBnWDUzTmp2Y2t5c1Y2eFhDaTM4US9ma3kyOWFOYlRaZWMwS0pBT0tWdm5jV3ZrSlBnS3YxMGtqVWhlYm89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=TfGuf19VHH63qLSqADaaJm4NOxaUDYsGUGj1NEJ3Yvszid8o9x3AqGiCv8TPu9x5N5TWHY5YHL3ldNJy1GYRiCzkaDqsggrpsewCDoh3Xi9tZ4ozWQ==; tt_scid=L6QXcXZTq2VFep-TBAGuFCzCw4xVzxMu0EvSOUcSrz3BrOACDqhr0MkUOZ43-Sra1c02; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAATPcUoavSkQERUQOqmvDXa8D-0BGak3Fhyg_RJdu530Bu8Mz3_dyTIdNzr606BFhX',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
user_id = 'MS4wLjABAAAATPcUoavSkQERUQOqmvDXa8D-0BGak3Fhyg_RJdu530Bu8Mz3_dyTIdNzr606BFhX'
response = requests.get(
    f'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={user_id}&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=4&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7318571700286735882&msToken=zzsRDJAi7Ai3lZiVYmoXX-QTtQak2yfl4FjzypBxpW6nv_aTKOAtCoX7fkeTOQc-5g09xi-HIgDXP0DSp5Uj4QXfV9F4ULPT5blgtViFk0aWQRbkEg==&X-Bogus=DFSzswVY15bANG//t7f/YkB9PiFB',
    headers=headers,
)
resp_json = response.json().get('aweme_list')
video_list = [item.get('video').get('play_addr').get('url_list')[0] for item in resp_json]

print(video_list)
for i, url in enumerate(video_list):
    print(f"准备下载{i}")
    with open(f"美女{i}.mp4", 'wb') as f:
        f.write(requests.get(url).content)
    break
