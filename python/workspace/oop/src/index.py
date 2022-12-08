#-*- coding:utf-8-*-
'''
Created on 2016-4-19

@author: Administrator
'''
class Provice:
    
    #静态字段
    meno = "中国的23个省之一"
    
    def __init__(self,name,capital,leader):
        
        self.Name = name
        self.Capital = capital 
        self.Leader = leader
        
    def sports_meet(self,sdd=0):
        print self.Name +"     正在开运动会"
    
    #静态方法
    @staticmethod
    def Foo():
        print '每个省要带头反腐'
        
    #访问方式  hb.Bar
    @property
    def Bar(self):    
        print self.Name  
        return "something"
              
hb = Provice('河北','石家庄','yiyang')

#print hb.Capital
#print hb.meno
hb.sports_meet()
hb.Foo()
Provice.Foo()

hb.Bar
#print help(hb.sports_meet())