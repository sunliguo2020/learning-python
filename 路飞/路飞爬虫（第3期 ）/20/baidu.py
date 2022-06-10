from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17272609'
API_KEY = 'h3Grp2xXGG0VeSAKlDL9gc4Q'
SECRET_KEY = 'WEEeDpICnzifwBAGF4QW4QiGgSb1u3ND'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('你好波波老师哈哈哈', 'zh', 1, {
    'vol': 5,
    'per':111
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
