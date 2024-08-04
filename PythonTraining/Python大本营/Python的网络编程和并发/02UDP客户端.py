# -*- coding: utf-8 -*-
"""
 @Time : 2024/8/4 8:38
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import socket
from socket import socket as Socket

client_socket = Socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 发送数据
    send_msg = input('客户端>')
    client_socket.sendto(send_msg.encode('utf-8'), ('127.0.0.1', 8080))

    # 接收数据
    msg, addr = client_socket.recvfrom(1024)
    print(f"来自客户端IP:{addr[0]},端口:{addr[1]}的消息：{msg}")

client_socket.close()
