# -*- coding: utf-8 -*-
'''
Created on 2016-8-21

@author: sunliguo
'''
import urllib
import urllib2
import json

def myurlopen(url,data):
    data = urllib.urlencode(data)
    request = urllib2.Request(url,data)
    content = urllib2.urlopen(request).read()
    return content

def tieta_task_finish():
    '''铁塔已完成任务'''
    url = "http://101.227.253.208:58090/itower/mobile/app/service?porttype=XUNJIAN_FINISH_TASK&v=73&userid=2734763&c=0"
    data = {
            "start":1,
            'limit':2000
            }
    '''
    返回所有的键：
currentCount
count
data_info
status
taskInfoList
totalPages
currentPage
  
    '''
    count =0 
    result = json.loads( myurlopen(url, data))
    for j in result['taskInfoList']:
        for i ,k in j.iteritems():
            print i,k 
        
        count +=1
        break
    print count

def tieta_task_unstart():
    '''铁塔未开始巡检任务'''
    url = "http://101.227.253.208:58090/itower/mobile/app/service?porttype=TASK_UNSTART_LIST&v=73&userid=2734763&c=0"
    data = {
            'start':1,
            "limit":2000           
            }
    result = json.loads(myurlopen(url,data))
    count = 0
    for j in result['taskInfoList']:
#         for i ,k in j.iteritems():
#             print i,k 
#         break
        print j['stationname']
        count +=1
    print count
    
def project_detail():
    url= "http://101.227.253.208:58090/itower/mobile/app/service?porttype=XUNJIAN_PROJECT_DETAIL&v=73&userid=2734763&c=0"
    data={
          'projectid':"5D68FC76819915D8D3532FB31BF73786",
          'taskid':"D2A7F785504D80C9CF73C0B6826C5DCF"
    }
    '''
{u'currentCount': 0, 
u'count': 0,
 u'imgList': [{u'url': u'http://101.227.253.208:58090/ftp/itower/inspectImage/2016-08-15/e84baef16f004053ab056758857a2f1b_shuiyin.jpg',
 u'lon': 119.162394, 
 u'photoaddress': u'\u4e2d\u56fd\u5c71\u4e1c\u7701\u6f4d\u574a\u5e02\u5bd2\u4ead\u533a\u660a\u6d77\u5927\u8857', 
 u'attachmentid': u'c703b9f3fc814ca5b6d3a9527aad056e', 
 u'lat': 37.022332, 
 u'path': u'/itower/inspectImage/2016-08-15/e84baef16f004053ab056758857a2f1b_shuiyin.jpg', 
 u'phototime': u'2016-08-15 12:34:23'}, 
 
 {u'url': u'http://101.227.253.208:58090/ftp/itower/inspectImage/2016-08-15/ed59fb5254df41c688ceefdc447cb2a4_shuiyin.jpg', u'lon': 119.162394, u'photoaddress': u'\u4e2d\u56fd\u5c71\u4e1c\u7701\u6f4d\u574a\u5e02\u5bd2\u4ead\u533a\u660a\u6d77\u5927\u8857', u'attachmentid': u'15656528218d4541965110c03b30a71b', u'lat': 37.022332, u'path': u'/itower/inspectImage/2016-08-15/ed59fb5254df41c688ceefdc447cb2a4_shuiyin.jpg', u'phototime': u'2016-08-15 12:34:05'}], u'data_info': u'\u6b63\u5e38', u'status': u'OK', u'totalPages': 0, u'currentPage': 0, u'model': {u'isfinish': u'Y', u'county': u'\u6ee8\u6d77\u533a', u'id': u'5D68FC76819915D8D3532FB31BF73786', u'city': u'\u6f4d\u574a\u5206\u516c\u53f8', u'sitename': u'\u6ee8\u6d77\u533a\u592e\u5b50\u6ee8\u6d77\u82b1\u56ed', u'projectname': u'\u5854\u57fa\u68c0\u67e5', u'st_sitesource': None, u'isshidden': u'N', u'taskid': u'D2A7F785504D80C9CF73C0B6826C5DCF', u'province': u'\u5c71\u4e1c\u5206\u516c\u53f8', u'devname': u'\u5854\u57fa\uff08\u767e\u8272\uff09', u'inspectcycle': u'4', u'endtime': u'2016-08-15 12:32:19', u'st_deviceid': u'37070300000011', u'remark': u'\u7b26\u5408\u8981\u6c42', u'request': u'1\u3001\u94c1\u5854\uff1a\u5854\u57fa\u65e0\u88c2\u7f1d\uff1b\u57fa\u7840\u94a2\u7b4b\u4e0d\u5f97\u5916\u9732\uff1b\u5854\u811a\u5305\u5c01\u826f\u597d\u3001\u5730\u811a\u87ba\u6813\u65e0\u5916\u9732\u73b0\u8c61\uff0c\u5468\u56f4\u662f\u5426\u6709\u79ef\u6c34\uff0c\u5854\u811a\u5e95\u677f\u662f\u5426\u4e0e\u57fa\u7840\u9762\u63a5\u89e6\u826f\u597d\u3002\r\n2\u3001\u62b1\u6746\uff1a\u6746\u57fa\u65e0\u677e\u52a8\u73b0\u8c61\u3002\u623f\u9876\u6845\u6746\u5e94\u786e\u4fdd\u5c4b\u9762\u65e0\u5f00\u88c2\u3001\u6e17\u6f0f\u3002', u'st_sitesource_dictvalue': None, u'begintime': u'2016-08-15 12:32:19', u'objtype': u'1', u'isstander': u'Y', u'shiddensource': None, u'sitecode': u'37070300000092'}}

    '''
    result = json.loads(myurlopen(url,data))
    print result

if __name__ == "__main__":
    project_detail()