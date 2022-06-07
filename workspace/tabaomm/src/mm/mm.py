#coding=utf-8
'''
Created on 2016-4-5

@author: Administrator
'''
import urllib2

mmurl = "https://mm.taobao.com/json/request_top_list.htm?type=0&page="

i=0
ph=-1
temp = '''<img src='''
while i<1 :
    url = mmurl +str(i)  
    i = i +1
    print url
    up =  urllib2.urlopen(url)
    cont = up.read()    
    print "----------------"
    #print cont  
    '''  
    head = "<img src"
    tail = ".jpg"
    ph = cont.find(head)   
    print "ph=" 
    print ph 
    pj=cont.find(tail,ph+1)
    #print cont[ph :pj + len(tail)]
    '''
    ahref = "<a href="
    atail = "target"
    
    ap = cont.find(ahref)
    aj = cont.find(atail,ap+1)    
    mm = "https:" + str(cont[ap+ len(ahref)+1:aj-2])
    print mm
    print urllib2.urlopen(mm).read()
    print "----------------"
