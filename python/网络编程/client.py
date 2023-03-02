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
        tcp_client.bind(('10.155.87.108', 99))
        tcp_client.connect((server_ip, server_port))
    except socket.error:
        print('fail to setup socket connection')
    else:
        print('sedding----')
        tcp_client.sendall(b'GET / HTTP/1.1\n\n')
        print('reading-----')
        print(tcp_client.recv(1024))
    tcp_client.close()


if __name__ == '__main__':
    dst_server = socket.gethostbyname('www.baidu.com')
    print('server:', dst_server)
    start_tcp_client('103.150.24.11', 441)
