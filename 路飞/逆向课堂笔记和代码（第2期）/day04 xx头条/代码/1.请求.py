import requests

res = requests.get(
    url="https://www.toutiao.com/api/pc/list/feed?channel_id=3189398957&max_behot_time=1642685645&category=pc_profile_channel&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00f01gfGxKAAAIDD-Yq4k6Rpx4oH6sAAAOAmr1zcfFgp6wmN73Rb5YObk9s-xG7dpC2shJNIvInOjEYhMJS1OV8iGNOVrpOl0wWoVDQEFxH3q9xU1Q.qAEgkZ0FNuc7otShtBXPe14",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
