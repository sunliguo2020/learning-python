import requests
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
def get_ids(play_url):
    import requests
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    #获取cid
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1UE411W7ZS&jsonp=jsonp'
    cid_ret_json = requests.get(url,headers=headers).json()
    cid = cid_ret_json['data'][0]['cid']
    #获取bvid
    #播放页的url
    play_page_url = play_url
    bvid = play_page_url.split('/')[-1]

    #获取aid
    aid_url = "https://api.bilibili.com/x/web-interface/view?cid=%s&bvid=%s"%(cid, bvid)
    res = requests.get(aid_url,headers=headers)
    res_json = res.json()
    aid = res_json['data']['aid']
    #播放量
    view_count = res_json['data']['stat']['view']
    #视频总时长
    duration = res_json['data']['pages'][0]['duration']  # 当前视频长度

    return cid,aid,bvid,view_count,duration

cid,aid,bvid,view, duration = get_ids('https://www.bilibili.com/video/BV1UE411W7ZS')


url = 'https://www.bilibili.com/video/BV1UE411W7fi?spm_id_from=333.999.0.0'
page_text = requests.get(url,headers=headers).text
ret = re.search('"stat":\{"aid":(?P<aid>\d+),"view":(?P<view>\d+),"danmaku',page_text)
#aid和播放量获取
print(ret.group("aid"),ret.group("view"))