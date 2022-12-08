#coding:utf-8
import json
import urllib.request
if __name__ == '__main__':
    url= "http://180.153.49.216:9000//billDeal/poweroffMonitor/listPoweroffMonitor.xhtml"
    sendData = {
        "AJAXREQUEST":"_viewRoot",
        "j_id164":"j_id164",
        "autoScroll":"",
        "javax.faces.ViewState":"j_id3",
        "unitid":"0106893",
        "j_id164:j_id165":"j_id164:j_id165",
        "AJAX:EVENTS_COUNT":"1"
    }
    header = {
              "Referer": "http://180.153.49.216:9000/billDeal/poweroffMonitor/listPoweroffMonitor.xhtml",
              "Accept-Encoding":" gzip, deflate",
              "Accept-Language": "zh-CN,zh;q=0.8",
              "Cookie": "JSESSIONID=5F8E8479E797773E9903BE4AB4F5C632"              
              }
    encode_data = urllib.parse.urlencode(sendData).encode('utf-8')
    print(encode_data)
    req = urllib.request.Request(url, encode_data)
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        res_data = response.read()
        print(res_data)
        #str_data = json.loads(res_data)
        #print(str_data)
    else:
        print(response.getcode())