#coding=utf-8
import json
#import urllib
import urllib.request

#钉钉机器人发信息

def dingtalk(str):
    #构建url
    url = "https://oapi.dingtalk.com/robot/send?access_token=8a7d8b3d0a75f70c6e32c80a545ac5e233dd18cecb579443f44d261663448c59"
    #构建头部
    header = {
              "Content-type":"application/json",
              "Charset":"utf-8"          
              }
    #3:构建我们的数据
    sendData = {
            "msgtype":"text",
            "text":{
                    "content":str               
                    },
            "at":{
                  "isAtall":True
                  }        
            }
    #对请求的数据进行json封装
    sendData = json.dumps(sendData)
    #sendData = urllib.parse.urlencode(sendData)
    sendData=bytes(sendData,'utf8') 
    #print(sendData) 
    
    #5发送请求
    req = urllib.request.Request(url,data=sendData,headers=header)
    response =urllib.request.urlopen(req)
    
    if response.getcode() == 200:
        res_data = response.read()
        str_data = json.loads(res_data)
        print(str_data)
    else:
        print(response.getcode())

if __name__ == "__main__":
    dingtalk("钉钉机器人测试")