#coding:utf-8

import itchat2

from myurlopen import myurlopen

get_alarm_list_url = "http://180.153.49.253:58090/itower/mobile/app/service?porttype=FSU_ALARM_LIST&v=111&userid=43361453&c=0"

rec_data = myurlopen(get_alarm_list_url)
#print(rec_data)
for key,value in rec_data.items():
    print(key,"value:",value)
    
for i  in rec_data['alarmList']:
    for key,value in i.items():
        print(key,":",value)
        
    print("\n\n")
