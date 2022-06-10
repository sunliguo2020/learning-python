import time
import uuid
import requests


def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time() * 1000 % 1e5))
    time_sec = time_sec.rjust(5, "0")

    return "{}{}infoc".format(uuid_sec, time_sec)


def get_video_info(bvid):
    session = requests.Session()
    res = session.get(
        url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid),
    )
    cid = res.json()['data'][0]['cid']

    res = session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid),
    )
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    # total_duration = res_json['data']['duration'] # 总时长
    duration = res_json['data']['pages'][0]['duration']  # 当前视频长度
    session.close()

    return aid, bvid, cid, view_count, duration


video_url = "https://www.bilibili.com/video/BV1XA411779D"

session = requests.Session()

# 1.获取buvid3
res = session.get(
    url=video_url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
)

# 2.生成uuid
_uuid = gen_uuid()
session.cookies.set('_uuid', _uuid)

# 3.固定的那几个cookie
session.cookies.set("CURRENT_FNVAL", "2000")
session.cookies.set("blackside_state", "1")

# 4.获取各种ID
buvid = video_url.rsplit("/")[-1]
aid, bvid, cid, view_count, duration = get_video_info(buvid)

# 5.发送请求获取sid cid=244573859&aid=329919014&bvid=BV1XA411779D
session.get(
    url="https://api.bilibili.com/x/player/v2",
    params={
        "cid": cid,
        "aid": aid,
        "bvid": bvid,
    }
)

# 6.发送now请求
res = session.get(
    url="https://api.bilibili.com/x/click-interface/click/now?jsonp=jsonp"
)

print(res.text)
# {"code":0,"message":"0","ttl":1,"data":{"now":1641911150}}
# {"code":0,"message":"0","ttl":1,"data":{"now":1641911108}}
