# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree

class index:
    def GET(self):
        return "hello"

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #return "weixin"
        #获取输入参数
        data = web.input()        
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #return signature,nonce,echostr
        #自己的token
        token="sgtietakey" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        s = ''.join(list)
        hashcode = hashlib.sha1(s).hexdigest()   

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
    def mypoPOST(self):
        str_xml=web.data()
        xml = etree.fromstring(str_xml)
        content=xml.find("Content").text
        msgType=xml.find("MsgType").text
        fromUser=xml.find('FromUserName').text
        toUser = xml.find('TouserName').text
        return self.render.reply_text(fromUser,toUser,int(time.time()),u"我现在还在开发中"+content)

    def POST(self):
        #str_xml = web.data() #获得post来的数据
        #xml = etree.fromstring(str_xml)#进行XML解析
        #content=xml.find("Content").text#获得用户所输入的内容
        #msgType=xml.find("MsgType").text
        #fromUser=xml.find("FromUserName").text
        #toUser=xml.find("ToUserName").text
        #return self.render.reply_text(fromUser,toUser,int(time.time()),u"我现在还在开发中，还没有什么功能，您刚才说的是："+content)
        return ''
