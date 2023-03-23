# *_* coding : UTF-8 *_*
# 文件名称   ：removal_of_interference_data.py
# 开发工具   ：PyCharm
import requests    # 导入网路请求模块
from get_stations import read  # 自定义读取文件方法
from get_stations import isStations # 自定义判断文件是否存在的方法
from prettytable import PrettyTable # 美化表格库


data = []  # 用于保存整理好的车次信息


def query(date, from_station, to_station):
    data.clear()  # 清空数据
    stations = eval(read())  # 读取所有车站并转换为dic类型
    place_of_departure = stations[from_station]  # 在所有车站文件中找到对应的参数，出发地
    destination = stations[to_station]           # 目的地
    # 查询请求地址
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.' \
          'train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.' \
          'to_station={}&purpose_codes=ADULT'.format(
        date, place_of_departure, destination)
    # 发送查询请求
    response = requests.get(url)
    # # 将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    # 判断车站文件是否存在
    if isStations() == True:
        stations = eval(read())  # 读取所有车站并转换为dic类型
        if len(result) != 0:  # 判断返回数据是否为空
            for i in result:
                # 分割数据并添加到列表中
                tmp_list = i.split('|')
                # 因为查询结果中出发站和到达站为站名的缩写字母，所以需要在车站库中找到对应的车站名称
                from_station = list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station = list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                # 创建座位数组，由于返回的座位数据中含有空既“”，所以将空改成--这样好识别
                seat = [tmp_list[3], from_station, to_station, tmp_list[8], tmp_list[9], tmp_list[10]
                    , tmp_list[32], tmp_list[31], tmp_list[30], tmp_list[21]
                    , tmp_list[23], tmp_list[33], tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                # 循环将座位信息中的空既“”，改成--这样好识别
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)  # 保存新的座位信息
                data.append(newSeat)
        return data  # 返回整理好的车次信息
if __name__ == '__main__':
    data_info=query('2019-04-09','北京','上海')
    table_header = ('车次 出发站 到达站 出发时间 到达时间 历时 '
                    '特等座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座').split()
    table = PrettyTable(table_header)  # 创建美化表格对象
    for i in data_info:               # 循环遍历每一条车次信息
        table.add_row(i)               # 每条数据添加至表格中
    print(table)                       # 打印表格
