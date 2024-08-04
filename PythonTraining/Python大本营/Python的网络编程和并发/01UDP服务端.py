# -*- coding: utf-8 -*-
"""
 @Time : 2024/8/4 8:38
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 实现 客户端和服务器的即时聊天
"""
import socket
from socket import socket as Socket

server_socket = Socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1', 8080))

while True:
    # 接收消息
    msg, addr = server_socket.recvfrom(1024)
    print(f"来自客户端IP:{addr[0]},端口:{addr[1]}的消息：{msg}")

    # 服务端发送消息
    send_msg = input('服务端>')
    server_socket.sendto(send_msg.encode('utf-8'),addr)

server_socket.close()