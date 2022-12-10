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

def get_sid(play_url):
    cid,aid,bvid,view, duration = get_ids(play_url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://api.bilibili.com/x/player/v2'
    params = {
        'cid':cid,
        'aid':aid,
        'bvid':bvid
    }
    response = requests.get(url,params=params,headers=headers)
    sid = response.cookies.get_dict()['sid']
    return sid

sid = get_sid("https://www.bilibili.com/video/BV1UE411W7ZS")
print(sid)