import requests

sessions  = requests.Session()
sessions.cookies['qf'] = 'qiaofu'
res = sessions.get('http://httpbin.org/get')
print(res.text)
print(res.cookies)