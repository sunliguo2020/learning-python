#-*- coding:utf-8-*-
'''
Created on 2016-4-29

@author: Administrator
'''
import urllib2,urllib
import cookielib

#EOSOperator%2FuserID=15653613197&EOSOperator%2Fpassword=tsdtsdhanhan926plfplf

data = {
        "EOSOperator/FuserID":'110',
        "EOSOperator/Fpassword":'tsd111plfplf'        
        }

url = 'http://61.156.3.60:9081/PB_COMMON.prCTGSLogin.login.do'
refer='http://61.156.3.60:9081/login.jsp'

cj = cookielib.CookieJar()  

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]  
urllib2.install_opener(opener)  
f= opener.open(refer)


req = urllib2.Request(url,urllib.urlencode(data))  

req.add_header("Referer",refer)
  
resp = urllib2.urlopen(req)  
print resp.read().decode('gb2312')

'''
POST /PB_COMMON.prCTGSLogin.login.do HTTP/1.1
Accept-Encoding: identity
Content-Length: 62
Host: 61.156.3.60:9081
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)
Connection: close
Referer: http://61.156.3.60:9081/login.jsp
Content-Type: application/x-www-form-urlencoded

EOSOperator%2FFpassword=tsd111plfplf&EOSOperator%2FFuserID=110HTTP/1.1 200 OK
Content-Type: text/html;charset=GBK
Content-Language: zh
Content-Length: 5461
Set-Cookie: JSESSIONID=0001foECrGmjrCNkUhvRQUYPo7n:IBPVFURND; Path=/
Set-Cookie: eos_style_cookie=default; Expires=Sun, 29 May 2016 06:14:36 GMT
Connection: Close
Date: Fri, 29 Apr 2016 06:14:36 GMT
Server: WebSphere Application Server/6.1
Expires: Thu, 01 Dec 1994 16:00:00 GMT
Cache-Control: no-cache="set-cookie, set-cookie2"

'''

'''
先打开一次refer f= opener.open(refer)
POST /PB_COMMON.prCTGSLogin.login.do HTTP/1.1
Accept-Encoding: identity
Content-Length: 62
Connection: close
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)
Host: 61.156.3.60:9081
Referer: http://61.156.3.60:9081/login.jsp
Cookie: JSESSIONID=0001zgT20fb7DQ99hdRp3DVUtnu:IBPVFURND
Content-Type: application/x-www-form-urlencoded

EOSOperator%2FFpassword=tsd111plfplf&EOSOperator%2FFuserID=110HTTP/1.1 200 OK
Content-Type: text/html;charset=GBK
Content-Language: zh
Content-Length: 5461
Set-Cookie: eos_style_cookie=default; Expires=Sun, 29 May 2016 06:18:21 GMT
Connection: Close
Date: Fri, 29 Apr 2016 06:18:21 GMT
Server: WebSphere Application Server/6.1
Expires: Thu, 01 Dec 1994 16:00:00 GMT
Cache-Control: no-cache="set-cookie, set-cookie2"

'''