import requests
import time
#播放页的url（即将要刷播放的视频）
play_url = 'xxx某视频的播放页urlxxx'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
#创建了一个新的session对象，该对象中暂无保存任何cookie
seesion = requests.Session()
#1.整合buvid3到session对象中
def get_buvid3(play_url):
    url = play_url
    seesion.get(url=url,headers=headers)
get_buvid3(play_url)

#2.整合uuid到session对象中
def get_uuid():
    import execjs
    node = execjs.get()
    fp = open('uuid.js','r',encoding='utf-8')
    ctx = node.compile(fp.read())
    uuid = ctx.eval('get_uuid()')
    return uuid
uuid = get_uuid()
#手动将一组cookie存储到session对象
seesion.cookies.set('_uuid',uuid)

#3.b_lsid整合到session对象中
def get_b_lsid():
    import execjs
    import time
    e = str(int(time.time() * 1000))
    node = execjs.get()
    fp = open('b_lsid.js','r',encoding='utf-8')
    ctx = node.compile(fp.read())
    lsid = ctx.eval('get_final_t("%s")'%e)
    return lsid
lsid = get_b_lsid()
seesion.cookies.set('b_lsid',lsid)

#4.sid整合到session对象中
def get_ids(play_url):
    # 获取bvid
    # 播放页的url
    play_page_url = play_url
    bvid = play_page_url.split('/')[-1]

    #获取cid
    url = 'https://api.bilibili.com/x/player/pagelist?bvid=%s&jsonp=jsonp'%bvid
    cid_ret_json = requests.get(url,headers=headers).json()
    cid = cid_ret_json['data'][0]['cid']


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
    seesion.get(url,params=params,headers=headers)
get_sid(play_url)

#剩下固定不变的cookie的整合
seesion.cookies.set('CURRENT_FNVAL',"4048")
seesion.cookies.set('buvid4','470CA30A-8DF5-92FC-931E-28D9C5E012C789949-022012421-e1+nZA0uNaJdA3gSdXO4dw%3D%3D')
seesion.cookies.set('buvid_fp','e201bfe1170d7011c37fc0c8c6e863e1')
seesion.cookies.set('blackside_state','0')
#至此cookie的整合结束
import random
cid,aid,bvid,view_count,duration = get_ids(play_url)
print('视频的原始播放：',view_count)
h5_url = 'https://api.bilibili.com/x/click-interface/click/web/h5'
ctime = int(time.time())
data = {
    "aid": aid,
    "cid": cid,
    "bvid": bvid,
    "part": "1",
    "mid": "0",
    "lv": "0",
    "ftime":str(ctime - random.randint(100,500)),
    "stime": str(ctime),
    "jsonp": "jsonp",
    "type": "3",
    "sub_type": "0",
    "from_spmid": "333.999.0.0",
    "auto_continued_play": "0",
    "refer_url":"" ,
    "bsource":"" ,
    "spmid": "333.788.0.0",
}
ret = seesion.post(h5_url,headers=headers,data=data).json()
print(ret)

cid,aid,bvid,view_count,duration = get_ids(play_url)
print('h5请求后的播放：',view_count)


