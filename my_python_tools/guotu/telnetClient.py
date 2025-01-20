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
    """
    TelnetClient类用于实现Telnet客户端的连接、登录、执行命令和登出功能。
    """
    def __init__(self):
        """
        初始化TelnetClient实例，创建telnetlib.Telnet对象。
        """
        self.tn = telnetlib.Telnet()

    def login_host(self, host_ip, host_port=23, username=None, password=None):
        """
          登录Telnet服务器。

          :param host: Telnet服务器的IP地址或主机名
          :param username: 登录用户名，默认为空
          :param password: 登录密码，默认为空
          :return: 如果登录成功返回True，否则返回False
          """
        try:
            self.tn.open(host_ip, port=host_port)
            # 根据服务器响应读取提示信息
            prompt = self.tn.read_until(b'Password:',timeout=10)
            if username is not None:
                self.tn.write(username.encode('ascii') + b'\n')
                prompt = self.tn.read_until(b'Password:').decode('ascii')
            if password is not None:
                self.tn.write(password.encode('ascii') + b'\n')
        except Exception as e:
            logging.warning(f"{host_ip}login failed")
            return False
        # 等待登录后的提示信息，确认是否登录成功
        self.tn.read_until(b'$ ').decode('utf-8')
        logging.info(f"Logged in to {host} successfully.")
        return True
        # 判断是否登陆成功
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
