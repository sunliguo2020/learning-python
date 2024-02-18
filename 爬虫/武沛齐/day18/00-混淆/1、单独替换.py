# -*- coding: utf-8 -*-
"""
 @Time : 2024/2/15 21:23
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import re
import subprocess


def exec_value(hex_string):
    res = subprocess.check_output(f"node xxx.js {hex_string}")
    char_string = res.decode('utf-8').strip()

    return char_string


def run():
    with open('f1.js', mode='r', encoding='utf-8') as f1, open('f2.js', mode='w', encoding='utf-8') as f2:
        # 遍历f1每一行
        for line in f1:
            if not line:
                print(f'空行:{line}')
                f2.write(line)
                continue
            match_list = re.findall(r"(RG\((.*?)\))", line)
            if match_list:
                print(f"match_list:{match_list}")
            for total, arg in match_list:
                real_value = exec_value(arg)
                line = line.replace(total, f'"{real_value}"')
            f2.write(line)


if __name__ == '__main__':
    run()
