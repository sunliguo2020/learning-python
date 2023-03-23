import os
import random

import wmi

sec = "t95p0q2f6dz1cxmowgjensr7yh384bvualki"
dec = "dn7vhlk3wx1efsyc56zu2bomjtq8i0g4rp9a"
c = wmi.WMI()
for physical_disk in c.Win32_DiskDrive():
    hard_seral = physical_disk.SerialNumber  # 获取硬盘序列号
    print("硬盘序列号为：", hard_seral)
if len(hard_seral) > 6:
    hard_seral = hard_seral[-6:]
else:
    print("硬盘信息获取错误！")
    os.exit(0)
for cpu in c.Win32_Processor():
    cpu_seral = cpu.ProcessorId.strip()  # 获取CPU序列号
    print("CPU序列号为：", cpu_seral)
if len(cpu_seral) > 4:
    cpu_seral = cpu_seral[-4:]
else:
    print("CPU信息获取错误！")
    os.exit(0)
for board_id in c.Win32_BaseBoard():
    board_id = board_id.SerialNumber  # 获取主板序列号
    print("主板序列号为：", board_id)
if len(board_id) > 6:
    board_id = board_id[-5:]
else:
    print("主板信息获取错误！")
    os.exit(0)
seral = hard_seral + cpu_seral + board_id
print("注册码使用的硬件信息为：", seral)
cha_seral = ""
for i in range(0, 14, 2):
    cha_seral += seral[14 - i] + seral[i + 1]  # 字符串尾和首递进连接生成新的字符串
cha_seral = cha_seral + seral[7]  # 字符串的中间值放到新字符串最后
list_seral = list(cha_seral)  # 字符串转为列表
list_seral.reverse()  # 列表反转
rand_seral = ""
for i in range(10):  # 将前10个字符串和其位置索引（16进制）连接
    j = random.randint(1, len(list_seral))
    rand_seral += hex(j)[2:] + list_seral[j - 1]  # hex(j)[2:] ，去掉16进制前的符号0x
    list_seral.remove(list_seral[j - 1])
rand_seral = ''.join(list_seral) + rand_seral  # 形成25位的字符串
low_seral = ""
rand_seral = rand_seral.lower()
for item in rand_seral:
    j = sec.index(item)
    low_seral += dec[j]
low_seral = low_seral.upper()
last_seral = low_seral[0:5] + "-" + low_seral[5:10] + "-" + low_seral[10:15] + "-" + low_seral[15:20] + "-" + low_seral[
                                                                                                              20:25]
print("生成的注册码为：\n", last_seral)
