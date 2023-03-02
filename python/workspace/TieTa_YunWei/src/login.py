# -*- coding: utf-8 -*-
'''
Created on 2016-8-8

@author: sunliguo
'''
import urllib,urllib2,cookielib
import json

loginUrl = "http://101.227.240.110:8989/baf/jsp/uiframe/login.jsp"
logPostUrl = "http://101.227.240.110:8989/jf/login/checkLogin"
CaptchaUrl = "http://101.227.240.110:8989/servlet/ValidateCodeServlet "
 
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
 
#urllib2.urlopen(loginUrl)
# print "cookie =" ,cookie

#首先获取验证码，人工分析
CapPicReq = urllib2.urlopen(CaptchaUrl)
with open("cappic.jpg","wb") as f:
    f.write(CapPicReq.read()) 
code = raw_input("输入验证码：")
loginData = {'loginName':'wangjianbo',
             'password':'w05368053',
             'picCode':code}
loginDataEncode = urllib.urlencode(loginData)

print "loginDataEncode = ",loginDataEncode

res = urllib2.urlopen(logPostUrl,loginDataEncode)
# with open("login.html","w") as f:
#     f.write(res.read())
# print "cookie = ",cookie

'''
status = {  "-2" : "用户名密码不正确！",
            "-1" : "登录失败，账号不存在！",
            1  : "OK",
            2  : "您的密码已到期，请修改密码！",
            3  : "验证码输入错误！",
            4  : "强制修改密码",
            51 : "登录失败！系统要求绑定IP地址登录，请绑定IP地址！",
            52 : "登录失败！您的登录IP与您绑定的IP不符！",
            6  : "动态密码不正确，请点击获取!",
            7  : "动态密码不正确，请重新输入!",
            8  : "当前人员必须通过统一认证系统登录！",
            9  : "有多个部门需选择一个",
            10 : "您已经被选为试运行发布测试用户，系统将自动跳转到试运行服务器，请重新输入密码登录!",
            11 : "密码不能再错一次，否则被锁定!",
            12 : "输入密码错误次数"+3+"次被锁!解锁请联系管理员！",
            13 : "您登陆的IP地址已经被限制登陆，请联系管理员解除限制！"
        };
'''
logJson = json.loads( res.read())
print logJson
if  logJson['status'] == '1':
    print "登录成功"
elif logJson['status'] == 3:
    print "验证码输入错误，重新输入"


'''
FSU实时查询的postdata
AJAXREQUEST=_viewRoot&queryForm=queryForm&queryForm%3AaddOrEditAreaNameId=%E5%AF%BF%E5%85%89%E5%8F%B0%E5%A4%B4%E5%8C%97%E6%B4%8B%E5%A4%B4&queryForm%3Aaid=4411E44F64ECA8B27595D630E091B32A&queryForm%3Afsuid=&queryForm%3AdeviceName=%E5%AF%BF%E5%85%89%E5%8F%B0%E5%A4%B4%E5%8C%97%E6%B4%8B%E5%A4%B4%2F%E5%BC%80%E5%85%B3%E7%94%B5%E6%BA%9001&queryForm%3Adid=37078340600687&queryForm%3AmidName=&queryForm%3Amid=&queryForm%3ApanelOpenedState=&javax.faces.ViewState=j_id10&queryForm%3Aj_id21=queryForm%3Aj_id21&AJAX%3AEVENTS_COUNT=1&

寿光台头北洋头
AJAXREQUEST=_viewRoot&
queryForm=queryForm&
queryForm:addOrEditAreaNameId=寿光台头北洋头&
queryForm:aid=4411E44F64ECA8B27595D630E091B32A&
queryForm:fsuid=&
queryForm:deviceName=寿光台头北洋头/开关电源01&
queryForm:did=37078340600687&
queryForm:midName=&
queryForm:mid=&
queryForm:panelOpenedState=&
javax.faces.ViewState=j_id10&
queryForm:j_id21=queryForm:j_id21&AJAX:EVENTS_COUNT=1&


寿光北洛工业园
AJAXREQUEST=_viewRoot&
queryForm=queryForm&
queryForm:addOrEditAreaNameId=寿光北洛工业区&
queryForm:aid=022606855&
queryForm:fsuid=&
queryForm:deviceName=寿光北洛工业区机房01/开关电源01&
queryForm:did=37078340600611&
queryForm:midName=&
queryForm:mid=&
queryForm:panelOpenedState=&
javax.faces.ViewState=j_id7&
queryForm:j_id21=queryForm:j_id21&AJAX:EVENTS_COUNT=1&


不同的有3个参数
queryForm:addOrEditAreaNameId=$查询的基站名称
queryForm:aid= 
queryForm:deviceName=$基站的设备名称
queryForm:did= $设备运维ID
javax.faces.ViewState=


AJAXREQUEST=_viewRoot&
queryForm=queryForm&
queryForm:addOrEditAreaNameId=寿光台头北洋头&
queryForm:aid=4411E44F64ECA8B27595D630E091B32A&
queryForm:fsuid=&
queryForm:deviceName=寿光台头北洋头/开关电源01&
queryForm:did=37078340600687&
queryForm:midName=&
queryForm:mid=&
queryForm:panelOpenedState=&
javax.faces.ViewState=j_id3&
queryForm:j_id21=queryForm:j_id21&
AJAX:EVENTS_COUNT=1&

'''

fsuShiShiUrl ="http://101.227.240.110:8989/business/resMge/pwMge/realTimePerformanceMge/realTimeperfdata.xhtml"

postData = {
'AJAXREQUEST':'_viewRoot',
'queryForm':'queryForm',
'queryForm:addOrEditAreaNameId':'寿光台头北洋头',
'queryForm:aid':'4411E44F64ECA8B27595D630E091B32A',
'queryForm:fsuid':'',
'queryForm:deviceName':'寿光台头北洋头/开关电源01',
'queryForm:did':'37078340600687',
'queryForm:midName':'',
'queryForm:mid':'',
'queryForm:panelOpenedState':'',
'javax.faces.ViewState':'j_id3',
'queryForm:j_id21':'queryForm:j_id21',
'AJAX:EVENTS_COUNT':'1'
}

req = urllib2.Request(fsuShiShiUrl,urllib.urlencode(postData))

print urllib.urlencode(postData)

content = urllib2.urlopen(req)

print content.read()