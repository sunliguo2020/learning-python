# -*- coding: utf-8 -*-
'''
Created on 2016-8-19

@author: sunliguo
'''
import urllib,urllib2
url = "http://tieta.applinzi.com/weixin"

postdata = '''<xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName> 
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>'''
 
print type(postdata)
 
 
req = urllib2.urlopen(url,(postdata))

print req.read()