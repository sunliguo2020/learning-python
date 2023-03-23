import datetime
print(" 高考倒计时 " )
now = datetime.datetime.today()                            #  获取当前日期
print("  今天是:", now.strftime("%Y-%m-%d %A "))
time1 = datetime.datetime(2021,6,7)                              # 2021年高考日期
time2 = datetime.datetime(2022,6,7)                              # 2022年高考日期
print("距离2021年高考还有"  + str((time1-now).days) +"天")
print("距离2022年高考还有"  + str((time2-now).days) +"天")
