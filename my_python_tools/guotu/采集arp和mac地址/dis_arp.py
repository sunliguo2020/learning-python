# -*- coding: utf-8 -*-
"""
 @Time : 2025/1/18 19:17
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import os
import sys
import time

from telnetClient import TelnetClient

if __name__ == '__main__':
    host = '10.155.88.254'
    password = 'Sggt@2019'
    command = 'dis arp'
    telnet_client = TelnetClient()

    if not telnet_client.login_host(host, password=password):
        print('登录失败')
        sys.exit(1)

    result = telnet_client.execute_some_command(command)
    # 获取当前日期并创建文件夹
    current_date = time.strftime('%Y-%m-%d', time.localtime())
    folder_path = os.path.join(f'{host}_arp', current_date + '_arp')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 文件名包含时间戳
    mytime = time.strftime('%Y%m%d%H%M%S', time.localtime())

    file_path = os.path.join(folder_path, "10.155.88.254_{}_arp.log".format(mytime))

    with open(file_path, 'w') as fp:
        fp.write(result)

    telnet_client.logout_host()
