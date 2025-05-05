# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/5/5 15:09
"""
import socket
import requests


def check_port(host, port=80, timeout=3):
    """检测指定端口是否开放"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0  # 返回 True 表示端口开放
    except Exception as e:
        print(f"端口检测异常: {e}")
        return False


def test_http_request(host, port=80, timeout=3):
    """发送 HTTP GET 请求测试"""
    try:
        url = f"http://{host}:{port}"
        response = requests.get(url, timeout=timeout)
        print(f"HTTP 响应状态码: {response.status_code}")
        print(f"服务器类型: {response.headers.get('Server', '未知')}")
        print(f"{response.headers}")
        print(f"{response.text}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"HTTP 请求失败: {e}")
        return False


if __name__ == "__main__":
    target_host = input("请输入目标主机IP或域名 (例如 192.168.1.1 或 example.com): ").strip()

    # 检测80端口
    print(f"\n检测 {target_host} 的80端口...")
    if check_port(target_host):
        print("✅ 80端口已开放！")

        # 发送HTTP请求测试
        print("\n尝试发送HTTP请求...")
        test_http_request(target_host)
    else:
        print("❌ 80端口未开放或无法连接。")