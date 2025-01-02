# -*- coding: utf-8 -*-
"""
 @Time : 2025/1/2 19:28
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import time
import ping3
import datetime

# 配置监控的IP地址和ping的时间间隔（秒）
IP_ADDRESS = '8.8.8.8'  # 替换为你想要监控的IP地址
INTERVAL = 5  # 每5秒ping一次

# 用于记录状态变化的时间点
state_changes = []
current_state = None  # 初始状态为空
last_response = None  # 用于跟踪上一次的ping响应

try:
    while True:
        response = ping3.ping(IP_ADDRESS)
        current_time = datetime.datetime.now()

        if response is None:
            # IP不可达
            if current_state != 'unreachable':
                # 如果当前状态不是unreachable，则记录状态变化的时间点
                if current_state == 'reachable':
                    # 从可达变为不可达
                    state_changes.append(('reachable_to_unreachable', current_time))
                current_state = 'unreachable'
        else:
            # IP可达
            if current_state != 'reachable':
                # 如果当前状态不是reachable，则记录状态变化的时间点
                if current_state == 'unreachable':
                    # 从不可达变为可达
                    state_changes.append(('unreachable_to_reachable', current_time))
                current_state = 'reachable'

        # 休眠指定的时间间隔
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    # 用户中断程序时，不需要额外处理，因为我们已经记录了所有的状态变化
    pass

finally:
    # 输出结果
    print("\n状态变化记录:")
    for change, timestamp in state_changes:
        print(f"{timestamp}: {change}")
