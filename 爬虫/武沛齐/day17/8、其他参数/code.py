# -*- coding: utf-8 -*-
"""
 @Time : 2024/1/31 21:57
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import re
import subprocess


def cmd(hex_arg):
    # hex_arg = '0x13a'
    res = subprocess.check_output(f"node demo.js {hex_arg}", shell=True)
    res_string = res.decode('utf-8').strip()
    # print(res_string)
    return res_string


def run():
    with open('f1.js', 'r', encoding='utf-8') as fr, open('f2.js', mode='w', encoding='utf-8') as fw:
        for line in fr:

            match_list = re.findall("(_0x425d8a\((.*?)\))", line)
            print(match_list)
            if not match_list:
                fw.write(line)
                continue

            for func_string, hex_arg in match_list:
                line = line.replace(func_string, f'"{cmd(hex_arg)}"')
            fw.write(line)
            # fw.write(line)


if __name__ == '__main__':
    run()
