#coding:utf-8
import myurlopen

DEBUG = 0

def reply_jiangkongxiang_list():
    #获取监控箱工单信息列表和未接单工单列表
    billListUrl="http://180.153.49.253:58090/itower/mobile/app/service?porttype=GET_BILL_MONITOR_LIST&v=111&userid=43361453&c=0"
    #工单状态信息
    billStatusDict ={
                     "ELECTRIC_JUDGE":"待发电",
                     "ACCEPT":"待接单",
                     "REVERT":"待回单",
                     "ELECTRIC_JUDGE":"待发电",
                     "ISSTAND":"待上站",
                     "alarmactivecount":"0:告警已消除，1告警未消除"
                     }
    
    str_data = myurlopen.myurlopen(billListUrl)    
    print(str_data)
    
    if DEBUG == 1:
        for i in str_data['billList']:
            for key,value in i.items():
                print(key,":",value)
    
    if str_data['data_info'] == "正常" and str_data['count'] >=1:
        
        str1 = "总共有"+str(str_data['count'])+"条工单信息"+'\n\n' 
        str2=''
        Daijiedan =[]
        for i in str_data['billList']:
            #获取billstatus 状态
            
            if i['billstatus'] == "ACCEPT":
                Daijiedan.append(i["stationname"])
                
            if i['billstatus'] not in billStatusDict:
                billstatus = i["billstatus"]
            else:
                billstatus = billStatusDict[i['billstatus']]
                
            if i["alarmactivecount"] ==0:
                alarm="告警已消除"
            elif i['alarmactivecount'] == 1:
                alarm="告警未消除"
            else:
                alarm="未知定义"
                
            str2=str(i['rownum_'])+":"+i['billtitle']+" "+alarm+" "+billstatus+"("+i['billstatus']+")"+"\n"+i['stationname']+'\n\n'+str2
        
        str3=str1+str2
        
        return str3,Daijiedan        
        #ding_jqr.dingtalk(str3)
        
    elif str_data['count'] == 1:
        print("没有工单信息")
        
        return "没有工单信息",[]

if __name__ == "__main__":
    print("dfaasf")
    result = reply_jiangkongxiang_list()
    print(result)