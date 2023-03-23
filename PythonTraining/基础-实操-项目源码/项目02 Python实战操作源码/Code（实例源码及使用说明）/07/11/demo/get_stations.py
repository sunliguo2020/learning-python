import re
import  requests
import os

def getStation():
    # 发送请求获取所有车站名称,通过输入的站名称转化查询地址的参数
    # url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006'
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050'
    response = requests.get(url, verify=True)  # 请求并进行验证
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)  # 获取需要的车站名称
    stations = dict((stations), indent=4)  # 转换为dic
    stations = str(stations)  # 转换为字符串类型否则无法写入文件
    write(stations)           #调用写入方法
def write(stations):
    file = open('stations.text', 'w', encoding='utf_8_sig')  # 以写模式打开文件
    file.write(stations)  # 写入数据
    file.close()
def read():
    file = open('stations.text', 'r', encoding='utf_8_sig')  # 以写模式打开文件
    data = file.readline()                                  #读取文件
    file.close()
    return data

def isStations():
    isStations = os.path.exists('stations.text')      #判断车站文件是否存在
    return isStations



