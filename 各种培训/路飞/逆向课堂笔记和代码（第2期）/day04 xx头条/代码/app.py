import os
import requests
import subprocess
import execjs
import os

os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
with open('v20.js', mode='r', encoding='utf-8') as f:
    js = f.read()
JS = execjs.compile(js)

url = "https://www.toutiao.com/api/pc/list/feed?channel_id=3189398957&max_behot_time=1642685645&category=pc_profile_channel&aid=24&app_name=toutiao_web"
signature = JS.call("get_sign", url)
print(signature)
final_url = f"{url}&_signature={signature}"

res = requests.get(
    url=final_url,
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
