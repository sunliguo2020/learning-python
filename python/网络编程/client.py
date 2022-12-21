# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-21 22:09
"""
import socket


def start_tcp_client(ip, port):
    server_ip = ip
    server_port = port

    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp_client.bind(('192.168.110.7', 99))
        tcp_client.connect((server_ip, server_port))
    except socket.error:
        print('fail to setup socket connection')
    else:
        print('sedding----')
        tcp_client.sendall(b'GET / HTTP/1.1\n')
        print('reading-----')
        print(tcp_client.recv(1024))
    tcp_client.close()


if __name__ == '__main__':
    start_tcp_client("112.34.112.40", 80)
