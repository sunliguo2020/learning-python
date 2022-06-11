import time
import uuid
import random
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
    print(res.request.url)
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    # total_duration = res_json['data']['duration'] # 总时长
    duration = res_json['data']['pages'][0]['duration']  # 当前视频长度
    session.close()

    return aid, bvid, cid, view_count, duration


def play(video_url):
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

    # 4.获取各种ID + duration=时长
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
    # ctime = res.json()['data']['now']  # 不建议

    # print(res.text)
    # {"code":0,"message":"0","ttl":1,"data":{"now":1641911150}}
    # {"code":0,"message":"0","ttl":1,"data":{"now":1641911108}}

    # 7.h5请求 1641907696
    ctime = int(time.time())
    res = session.post(
        url="https://api.bilibili.com/x/click-interface/click/web/h5",
        data={
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "part": "1",
            "mid": "0",
            "lv": "0",
            "ftime": ctime - random.randint(100, 500),  # 浏览器首次打开时间
            "stime": ctime,
            "jsonp": "jsonp",
            "type": "3",
            "sub_type": "0",
            "from_spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource": "",
            "spmid": ""
        }
    )

    # 8.首次心跳
    session.post(
        url="https://api.bilibili.com/x/click-interface/web/heartbeat",
        data={
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "mid": "0",
            "csrf": "",
            "played_time": "0",
            "real_played_time": "0",
            "realtime": "0",
            "start_ts": ctime,
            "type": "3",
            "dt": "2",
            "play_type": "1",
            "from_spmid": "",
            "spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource": ""
        }
    )

    # 9.中间心跳，根据视频时长决定
    # 假如：60s  60/15 = 3 -> 15
    # 假如：65s  65/15 = 4 -> 5
    loop_count, div = divmod(duration, 15)
    if not div:
        loop_count = loop_count - 1
        div = 15

    for i in range(1, loop_count + 1):
        # time.sleep(15)
        # 发送一个请求
        # session.post(
        #     url="https://api.bilibili.com/x/click-interface/web/heartbeat",
        #     data={
        #         "aid": aid,
        #         "cid": cid,
        #         "bvid": bvid,
        #         "mid": "0",
        #         "csrf": "",
        #         "played_time": 15 * i,
        #         "real_played_time": 15 * i,
        #         "realtime": 15 * i,
        #         "start_ts": ctime,
        #         "type": "3",
        #         "dt": "2",
        #         "play_type": "0",
        #         "from_spmid": "",
        #         "spmid": "",
        #         "auto_continued_play": "0",
        #         "refer_url": "",
        #         "bsource": ""
        #     }
        # )

        # 生成一个任务发送到：参数 + cookie
        data_dict = {
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "mid": "0",
            "csrf": "",
            "played_time": 15 * i,
            "real_played_time": 15 * i,
            "realtime": 15 * i,
            "start_ts": ctime,
            "type": "3",
            "dt": "2",
            "play_type": "0",
            "from_spmid": "",
            "spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource": ""
        }
        cookie_dict = session.cookies.get_dict()
        exec_time = ctime + i * 15

    # 10.最后心跳
    time.sleep(div)

    session.post(
        url="https://api.bilibili.com/x/click-interface/web/heartbeat",
        data={
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "mid": "0",
            "csrf": "",
            "played_time": -1,
            "real_played_time": duration,
            "realtime": duration,
            "start_ts": ctime,
            "type": "3",
            "dt": "2",
            "play_type": "4",
            "from_spmid": "",
            "spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource": ""
        }
    )


def run():
    video_url = "https://www.bilibili.com/video/BV1XA411779D"

    bvid = video_url.rsplit('/')[-1]
    aid, bvid, cid, view_count, duration = get_video_info(bvid)
    print("播放数量：", view_count)

    # 播放
    play(video_url)


if __name__ == '__main__':
    run()
