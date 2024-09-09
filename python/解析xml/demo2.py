# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-04-25 19:12
"""
import xml.etree.ElementTree as ET

with open(r'D:\睿智\世纪学校\世纪东城\世纪东城监控\世纪东城杂牌监控软件\雄迈\20240425_185819_Device.xml', 'r', encoding='utf-8') as fp:
    xml_string = fp.read()
root = ET.fromstring(xml_string)

for device in root.findall('Device'):
    ip_address = device.get('IP')
    if ip_address:
        print(ip_address)