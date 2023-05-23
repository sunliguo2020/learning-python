# 连接wifi
# socket udp
# 接受udp数据
# 根据接收到的UDP数据控制led亮灭
import time
import machine

def do_connect():
    """
    链接wifi
    """
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ruizhixinxi', 'ruizhi2016')
        i = 1
        while not wlan.isconnected():
            print(f"正在链接网络---{i}")
            time.sleep(1)
            i = i+1
    print('network config:', wlan.ifconfig())
def create_udp_socket():
    import socket
    # 1、创建udpsocket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2、绑定固定的端口
    udp_socket.bind(("0.0.0.0",7788))
    return udp_socket

    pass
def main():
    do_connect()
    udp_socket = create_udp_socket()
    # 创建GPIO引脚对象
    led = machine.Pin(12,machine.Pin.OUT)
    # 接收数据
    while True:
        recv_data,sender_info= udp_socket.recvfrom(1024)
        print(f"{sender_info}发送的数据:{recv_data}")
        
        recv_data_str = recv_data.decode("utf-8")
        print(f"解码后的数据:{recv_data_str}")
        
        if recv_data_str == 'light on':
            led.value(1)
        elif recv_data_str == 'light off':
            led.value(0)
        elif recv_data_str == 'light':
            led.value(not led.value())
if __name__ == "__main__":
    main()