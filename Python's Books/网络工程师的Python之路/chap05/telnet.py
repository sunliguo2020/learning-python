# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/6/17 13:42
"""
import telnetlib

host = '192.168.2.11'
user = 'python'
password = '123'

tn = telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b'Password:')
tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b'int loopback 1\n')
tn.write(b'ip address 1.1.1.1 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b"exit\n")

print(tn.read_all())
