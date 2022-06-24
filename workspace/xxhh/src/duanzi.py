# -*- coding: utf-8 -*-
'''
Created on 2016-8-12

@author: sunliguo
'''

duanzifile = open('d:/duzi.txt',"a+")
import urllib2,re
for j in xrange(10000):
    url = "http://www.xxhh.com/duanzi/page/%s/?l=1470981564" %j
    
    content = urllib2.urlopen(url)
    content =  content.read().decode('utf-8')
    
    #print content
    """<div class="article"><pre>班主任今天对我们说：我们班严禁异性在校期间谈恋爱！
    停了一下，又说：同性也不行！</pre></div>"""
    
    myItems=re.findall('<div.*?class="article"><pre>(.*?)</pre></div>',content)
    for i in  myItems:
        print i
        duanzifile.writelines(str(i.encode('utf-8')+'\n'))
