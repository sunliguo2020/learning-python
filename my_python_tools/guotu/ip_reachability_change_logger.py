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
LOG_FILE = 'state_changes.log'  # 状态变化日志文件

# 检查日志文件是否存在，如果不存在则创建它（实际上这个步骤可能不是必需的，因为打开文件时会自动创建）
try:
    with open(LOG_FILE, 'r') as file:
        # 这里只是检查文件是否存在，不需要读取内容
        pass
except FileNotFoundError:
    with open(LOG_FILE, 'w') as file:
        # 创建一个空文件（如果文件不存在的话，这个步骤在后面的写入操作中也会自动完成）
        pass

# 用于记录状态变化的时间点和类型
state_changes = []  # 这个列表现在仅用于在内存中临时存储状态变化，以便在程序中断时能够输出给用户看（如果需要的话）
current_state = None  # 初始状态为空

try:
    while True:
        response = ping3.ping(IP_ADDRESS)
        current_time = datetime.datetime.now()

        if response is None:
            # IP不可达
            if current_state != 'unreachable':
                # 如果当前状态不是unreachable，则记录状态变化并写入文件
                if current_state == 'reachable':
                    change_type = 'reachable_to_unreachable'
                else:
                    # 初始状态未知时，不记录从"未知"到"不可达"的变化（或者你可以决定如何记录它）
                    change_type = None

                if change_type:
                    # 记录到内存中的列表（可选，主要用于调试或程序中断时显示）
                    state_changes.append((change_type, current_time))
                    # 写入到日志文件
                    with open(LOG_FILE, 'a') as file:
                        file.write(f"{current_time}: {change_type}\n")
                current_state = 'unreachable'
        else:
            # IP可达
            if current_state != 'reachable':
                # 如果当前状态不是reachable，则记录状态变化并写入文件
                if current_state == 'unreachable':
                    change_type = 'unreachable_to_reachable'
                else:
                    # 初始状态未知时，不记录从"未知"到"可达"的变化（或者你可以决定如何记录它）
                    change_type = None

                if change_type:
                    # 记录到内存中的列表（可选，主要用于调试或程序中断时显示）
                    state_changes.append((change_type, current_time))
                    # 写入到日志文件
                    with open(LOG_FILE, 'a') as file:
                        file.write(f"{current_time}: {change_type}\n")
                current_state = 'reachable'

        # 休眠指定的时间间隔
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    # 用户中断程序时，不需要额外处理日志文件，因为我们已经使用了'a'模式进行追加写入
    pass
except Exception as e:
    # 捕获其他可能的异常，并写入日志文件（可选，但推荐用于调试）
    with open(LOG_FILE, 'a') as file:
        file.write(f"{datetime.datetime.now()}: An error occurred: {e}\n")
    raise  # 重新抛出异常以便上层调用者可以处理（如果需要）

finally:
    pass
    # 如果需要在程序中断时输出记录的状态变化，可以取消以下代码的注释
    # 但请注意，这样做可能会使日志文件变得冗余，因为日志文件已经包含了这些信息
    # print("\n状态变化记录（内存中）:")
    # for change, timestamp in state_changes:
    #     print(f"{timestamp}: {change}")

    # 在这里我们不需要对state_changes列表进行任何额外的处理，因为所有的状态变化都已经被写入到日志文件中了
    # 如果需要查看状态变化，只需查看日志文件即可