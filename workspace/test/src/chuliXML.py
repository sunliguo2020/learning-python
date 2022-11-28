# -*- coding: utf-8 -*-
'''
Created on 2016-7-13

@author: Administrator
'''
import sys
'''
try:    
    import xml.etree.cElementTree as ET  
except ImportError:    
    import xml.etree.ElementTree as ET 
try:
    tree = ET.parse("country.xml") #打开 xml文档
    root = tree.getroot()
except Exception,e:
    print "Eoor :cannot parse file:country.xml"
    sys.exit(1)
print root.tag,"---",root.attrib

for child in root:
    print child.tag,"---",child.attrib

print "*"*10
print root[0][1].text
print root[0].tag,root[0].text
print "*"*10  

for country in root.findall('country') :
    rank = country.find('rank').text
    name = country.get('name')
    print name,rank
'''
#from xml.dom.minidom import import parse
import xml.dom.minidom

#使用minidom解析器打开xml文档
DOMTREE = xml.dom.minidom.parse("3588567.txt")

Data = DOMTREE.documentElement
#if Data.hasAttribute("name"):
#   print "name element :%s" % Data.getAttribute("name")  
#print dir(Data)
#在集合中获取所有的国家 
#Countrys = Data.getElementsByTagName("entity")   

#print "name :%s" % Country.getAttribute("BUSI_NBR")

if Data.getElementsByTagName("BUSI_NBR"):
    Data.getElementsByTagName(i)[0]BUSI_NBR = Data.getElementsByTagName("BUSI_NBR")[0]
    print "BUSI_NBR IS ",BUSI_NBR.childNodes[0].data
else:
    print "Not find BUSI_NBR"
    
    
print "Prod_inst_td",Data.getElementsByTagName("PROD_INST_ID")[0].childNodes[0].data
print "Cust_name",Data.getElementsByTagName("CUST_NAME")[0].childNodes[0].data
print "INSTALL_ADDR",Data.getElementsByTagName("INSTALL_ADDR")[0].childNodes[0].data

'''for node in Data.getElementsByTagName("data").childNodes:
    if node.nodeType== node.ELEMENT_NODE:
        print node.nodeName

    if Data.getElementsByTagName("INSTALL_ADDR").nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
         print "install_addr",Data.getElementsByTagName("INSTALL_ADDR")'''

