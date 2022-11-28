#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/12 13:39
"""
import logging
import telnetlib
import time

logging.basicConfig(filename='telnet.log',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(message)s')


class TelnetClient(object):
    def __init__(self):
        self.tn = telnetlib.Telnet()

    def login_host(self, host_ip, host_port=23, username=None, password=None):
        try:
            self.tn.open(host_ip, port=host_port)
        except Exception as e:
            logging.warning(f"{host_ip}login failed")
            return False
        self.tn.read_until(b'Password:', timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        time.sleep(2)

        #判断是否登陆成功
        command_result = self.tn.read_very_eager().decode('ascii')
        if '%Username or password is invalid.' not in command_result:
            print("login success")
            return True
        else:
            print("login failed")

    def execute_some_command(self, command):
        print("exec command:", command)
        self.tn.write(command.encode('ascii') + b'\n')
        # time.sleep(2)

        command_result = self.tn.read_until(b'5500>', timeout=2).decode('ascii')
        if command_result.endswith('----'):
            for i in range(10):
                self.tn.write(b' ')

        command_result += self.tn.read_until(b"5500>", timeout=2).decode('ascii')

        return command_result.replace('^[[16D                ^[[16D', '').replace(' - --- More - ---', "")

    def logout_host(self):
        self.tn.write(b'quit\n')


if __name__ == '__main__':
    host = '10.155.88.254'
    password = 'Sggt@2019'
    command = 'dis arp'
    telnet_client = TelnetClient()
    if telnet_client.login_host(host, password=password):
        result = telnet_client.execute_some_command(command)
        # print(result)
        mytime = time.strftime('%Y%m%d%H%M%S', time.localtime())
        with open("10.155.88.254_" + mytime + "_arp.log", 'w') as fp:
            fp.write(result)
        telnet_client.logout_host()
