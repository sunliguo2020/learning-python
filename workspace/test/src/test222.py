# -*- coding: utf-8 -*-
'''
Created on 2016-8-20

@author: sunliguo
'''
# import urllib2
# with open('test.py',"wb") as fp:
#     print type(fp)
#     
# fp = urllib2.urlopen("http://www.baidu.com")
# if hasattr(fp, "read"):
#     print "fp has read"
#     fp.seek(0)
from fileinput import filename

log = open("logfile.txt","a")
print >> log,('Downloading from url')
log.close()
import logging

logging.basicConfig(level=logging.INFO,filename="mylog.log")
logging.info('starting program')
