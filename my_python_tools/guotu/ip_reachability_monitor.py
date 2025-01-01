# -*- coding: utf-8 -*-
"""
 @Time : 2025/1/1 18:18
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import time
import ping3
import datetime

# 配置监控的IP地址和ping的时间间隔（秒）
IP_ADDRESS = '8.8.8.8'  # 替换为你想要监控的IP地址
INTERVAL = 5  # 每5秒ping一次

# 用于记录ping通和ping不通的时间
reachable_times = []
unreachable_times = []
current_state = None  # 初始状态为空
start_time = None

try:
    while True:
        response = ping3.ping(IP_ADDRESS)
        current_time = datetime.datetime.now()

        if response is None:
            # IP不可达
            if current_state != 'unreachable':
                # 如果当前状态不是unreachable，则记录开始时间并改变状态
                if start_time is not None and current_state == 'reachable':
                    reachable_times.append((start_time, current_time))
                start_time = current_time
                current_state = 'unreachable'
                print(f"{current_time}: IP {IP_ADDRESS} is unreachable")
        else:
            # IP可达
            if current_state != 'reachable':
                # 如果当前状态不是reachable，则结束上一个不可达时间段并改变状态
                if start_time is not None and current_state == 'unreachable':
                    unreachable_times.append((start_time, current_time))
                start_time = current_time
                current_state = 'reachable'
                print(f"{current_time}: IP {IP_ADDRESS} is reachable")

        # 休眠指定的时间间隔
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    # 用户中断程序时，处理最后一个时间段
    if current_state == 'unreachable' and start_time is not None:
        unreachable_times.append((start_time, datetime.datetime.now()))
    elif current_state == 'reachable' and start_time is not None:
        reachable_times.append((start_time, datetime.datetime.now()))

finally:
    # 输出结果
    print("\nIP可达时间段:")
    for start, end in reachable_times:
        print(f"从 {start} 到 {end}")

    print("\nIP不可达时间段:")
    for start, end in unreachable_times:
        print(f"从 {start} 到 {end}")
