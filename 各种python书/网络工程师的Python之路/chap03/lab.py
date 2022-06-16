# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/16 13:54
"""
print('''请根据对应的号码选择一个路由协议：
1.RIP
2.IGRP
3.EIGRP
4.OSPF
5.ISIS
6.BGP''')
option = input("请输入的你的选项（数字1-6）：")
if option.isdigit() and int(option)in list(range(1,7)):
    if int(option) in list(range(1,4)):
        print("该路由协议属于距离矢量路由协议")
    elif int(option) in list(range(4,6)):
        print("该路由协议属于链路状态路由协议")
    else:
        print("该路由协议属于路径矢量路由协议")
else:
    print('选项无效，程序终止')