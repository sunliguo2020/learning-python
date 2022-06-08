# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/4/11 14:52
"""
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import datetime
import telnetlib
import time

now = datetime.datetime.now()
host = "10.155.88.254"
passwd = "Sggt@2019\n"


#
def Output(ip, msg):
    """

    :param ip:
    :param msg:
    :return:
    """
    filename = "{0}_{1}_{2}_{3}_{4}_{5}_{6}_arp.log".format(ip, now.year, now.month, now.day, now.hour, now.minute,now.second)

    with open('./10.155.88.254_arp/' + filename, 'w') as fp:
        fp.write(msg)


tn = telnetlib.Telnet(host, port=23, timeout=10)
# tn.set_debuglevel(2)
# print(tn.read_all())
tn.read_until(b"Password:")
tn.write(passwd.encode('utf-8'))

tn.write('dis arp\n'.encode('utf-8'))

i = True
output = ''
while i:
    ret = tn.read_until(b'---- More ----', 5)
    if ret.endswith(b'---- More ----'):
        output += ret.decode('utf-8').strip('---- More ----')
        for i in range(10):
            tn.write(b' ')
            time.sleep(0.1)
    else:
        output += ret.decode('utf-8')
tn.write('quit\n'.encode('utf-8'))

# print(tn.read_all())
tn.close()
# print('$'*33)
# print(output)
Output(host, output)
