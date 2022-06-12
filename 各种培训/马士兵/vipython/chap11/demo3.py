# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/8/19 11:04
"""
lst =[{'rating':[9.5,1559181],'id':1292720,'type':['剧情','爱情'],'title':'阿甘正传','actors':['汤姆-汉克斯']}]
name = input('请输入要查询的演员：')
for item in lst: #遍历列表
    act_list = item['actors']
    for i in act_list:
        if name in i:
            print(name+"出演了："+item['title'])
    '''         
        actors = movie['actors']
        if name in actors:
            print(name+'出演了：'+movie)'''