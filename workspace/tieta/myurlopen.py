#coding:utf-8
import urllib.request
import json
import socket

def myurlopen(url):
    #构建url     
    #url2= "http://180.153.49.253:58090/itower/mobile/app/service?porttype=GET_BILL_MONITOR_LIST&v=111&userid=43361453&c=0"
    #构建头部
    header = {
              "Content-type":"application/x-www-form-urlencoded",
              "Charset":"utf-8" ,
              "User-Agent": "Mozilla/5.0 (Linux; Android 9.1.1; 20171212 Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3883.91 Mobile Safari/537.36"         
              }
    #3:构建我们的数据
    sendData = {
           "start":1,
           "limit":20  
            }
    
    #对请求的数据进行json封装
    sendData = urllib.parse.urlencode(sendData).encode(encoding='utf_8')
    #5发送请求
    req = urllib.request.Request(url,data=sendData,headers=header)
    
    timeout = 2 
    socket.setdefaulttimeout(timeout)
    
    try:
        response =urllib.request.urlopen(req)
    except  urllib.error as e:
        print("dddd")
        
    if response.getcode() == 200:
        res_data = response.read()
        str_data = json.loads(res_data)
        return str_data
    else:
        return response.getcode()

if __name__ == "__main__":        
    myreturn = myurlopen("http://180.153.49.25:58090/itower/mobile/app/service?porttype=FSU_ALARM_LIST&v=111&userid=43361453&c=0")
    print(myreturn)