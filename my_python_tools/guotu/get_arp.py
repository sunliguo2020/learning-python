#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/12 13:39
"""
import os
import time

from telnetClient import TelnetClient

if __name__ == '__main__':

    host = '10.155.88.254'
    password = 'Sggt@2019'
    command = 'dis arp'
    telnet_client = TelnetClient()
    try:
        if telnet_client.login_host(host, password=password):
            result = telnet_client.execute_some_command(command)
            mytime = time.strftime('%Y%m%d%H%M%S', time.localtime())
            # 创建以年月为名的目录
            year_month_dir = os.path.join(time.strftime('%Y-%m'), '')
            # 确保目录存在
            if not os.path.exists(year_month_dir):
                os.makedirs(year_month_dir)
            # 定义日志文件的名称，包含IP地址和时间戳
            filename = os.path.join(year_month_dir, f"10.155.88.254_{mytime}_arp.log")
            # 将结果写入日志文件
            with open(filename, 'w') as fp:
                fp.write(result)
        telnet_client.logout_host()
    except Exception as e:
        print(f"An error occurred: {e}")  # 异常处理
