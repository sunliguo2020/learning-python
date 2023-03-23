import time
import sys
leave=0                                      
print ("==========虚拟跑步机=========")
print (30 *"#")
weight=float(input("输入您的体重（kg）："))              # 输入的体重可以是浮点数                    
speed=float(input("速度（千米/小时）："))                # 输入的速度可以是浮点数
times=int(input("跑步时间（分钟）："))                    # 输入的跑步时间是整数，为分钟
times=times*60                                            # 将分钟转换为秒
while leave<times :                                      # 将分钟转换为秒
    leave+=1   
    min, sec = divmod(times-leave,60)                   # 将秒转换为分钟和秒
    leave_time=str(min)+'分'+str(sec)+'秒' 
    dista=leave/3600 * speed                             # 计算跑步距离
    calor =weight * 30/(400/(speed*1000/60)) * leave/60/60    # 计算热量
    sys.stdout.write('\r')
    sys.stdout.write('剩余时间:{}  跑步距离:{:.2f}千米  消耗热量:{:.2f} 千卡'.format(leave_time,dista,calor))
    sys.stdout.flush
    time.sleep(1)
