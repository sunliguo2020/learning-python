# -*- coding: utf-8 -*-
'''
Created on 2016-7-13

@author: sunliguo
'''
import xml.etree.ElementTree as ET

class MeituanParser:
    def __init__(self):
        self.meituan_deal_set=[]
    def parse(self,filepath):
        tree = ET.parse(filepath)
        #get root Element
        root = tree.getroot()
        #print root.tag,root.attrib
        
        for child in root:
            pass
            #print child.tag,"---",child.attrib
            
        for deal in root.findall('entity'):
            
            for child in deal:
                print child.tag,"---",child.attrib
            #deal=data.find('d')
            
            meituan_deal={}
            
            if deal is not None:
                try:
                    meituan_deal['USER_NAME']=deal.find('USER_NAME').text
                except Exception,exp:
                    print "No deal id"
                try:
                    meituan_deal['BUSI_NBR']=deal.find('BUSI_NBR').text
                    print meituan_deal['BUSI_NBR'].text
                    print "adfad"
                except Exception,exp:
                    print "imalid sales number"   
                self.meituan_deal_set(meituan_deal)
        return self.meituan_deal_set
    
    
if __name__ == "__main__":
    parser = MeituanParser()
    deal=parser.parse("15615363322.xml")
    for i in deal:
        print i