#coding:utf-8
import json
import urllib.request
if __name__ == '__main__':
    url= "http://180.153.49.253:58090/itower/mobile/app/service?porttype=GET_BILL_MONITOR_LIST&v=111&userid=43361453&c=0"
    sendData = {
    "start":"1",
    "limit":"20"
    }
    encode_data = urllib.parse.urlencode(sendData).encode('utf-8')
    req = urllib.request.Request(url, encode_data)
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        res_data = response.read()
        str_data = json.loads(res_data)
        print(str_data)
    else:
        print(response.getcode())