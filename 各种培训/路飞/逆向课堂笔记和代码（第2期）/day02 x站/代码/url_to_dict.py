url = "aid=850174341&cid=469991507&bvid=BV1xL4y1E78r&mid=0&csrf=&played_time=0&real_played_time=0&realtime=0&start_ts=1642084854&type=3&dt=2&play_type=1&from_spmid=&spmid=&auto_continued_play=0&refer_url=&bsource="

data_dict = {}
data_list = url.split("&")
for item in data_list:
    k, v = item.split('=')
    data_dict[k] = v

import json

res = json.dumps(data_dict, indent=2)
print(res)
