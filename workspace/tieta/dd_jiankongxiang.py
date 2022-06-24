#coding:utf-8
import ding_jqr
import tt_jiankongxiang
import time

def tick():
    print('Tick! The time is: %s' % time.now())
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
    
if __name__ == "__main__":
    second = sleeptime(0,20,20);
    
    while 1==1:                
        msg,Daijiedan = tt_jiankongxiang.reply_jiangkongxiang_list()
        print(msg)
        if len(Daijiedan) > 0:
            print("共有"+str(len(Daijiedan))+"条工单未接单:"+str(Daijiedan))
            ding_jqr.dingtalk("有未接工单!"+str(Daijiedan) )
        else :
            ding_jqr.dingtalk(msg)
                
        time.sleep(second);
