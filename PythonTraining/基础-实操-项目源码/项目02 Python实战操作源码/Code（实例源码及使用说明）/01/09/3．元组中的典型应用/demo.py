# *_* coding : UTF-8 *_*

# 文件名称   ：demo.py
# 开发工具   ：PyCharm
tuple1=(2,4,8,16,32,64,128,256,512,1024)         #  数字元组
tuple2=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec','Mon','Tues','Wed','Thur','Fri') #  月份、星期简写元组
tuple3=('勇士 57','掘金 54','开推者 53','火箭 53','爵士 50','雷霆 49','马刺 48','快船 48')
tuple4=(("肖申克的救赎",1994,9.3),("教父",1972,9.2),("教父2",1974,9.1),("蝙蝠侠：黑暗骑士",2008,9.0),("低俗小说",1994,8.9))   # 电影信息元组
tuple5=((90,128,87.103),(78,99,134.106),(98,102,133.80),(66,78,97,56),(98,123,88.79))
print(max(tuple2,key=lambda x:len(x)))    #  输出元组中长度最大的元组，输出结果为：Sept
print(max(tuple3,key=lambda x:x[-2:]))    #  输出结果为：勇士 57
print(max(tuple4,key=lambda x:x[1]))      #  输出结果为：('蝙蝠侠：黑暗骑士', 2008, 9.0)
print(max(tuple4,key=lambda x:x[2])[0])   #  输出结果为：肖申克的救赎
print(max(max(tuple5,key=lambda x:x[1]))) #  输出结果为：128
print(max(tuple5,key=lambda x:(x[0]+x[1]+x[2])))   #  输出结果为：(98, 102, 133.8)
print(max(tuple5,key=lambda x:(x[0],x[1])))   #  输出结果为：(98, 123, 88.79)
