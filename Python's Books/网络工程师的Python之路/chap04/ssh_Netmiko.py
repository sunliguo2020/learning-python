# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/17 19:36
"""
from netmiko import ConnectHandler

SW2 = {
    'device_type': 'cisco_iso',
    'ip': '192.168.2.12',
    'username': 'python',
    'password': "123"
}
connect = ConnectHandler(**SW2)
print('Successfully connected to ' + SW2['ip'])
config_commands = ['int loop 1', 'ip address 2.2.2.2 255.255.255.255']
output = connect.send_config_set(config_commands)
print(output)
result = connect.send_command('show run int loop  1')
print(result)
