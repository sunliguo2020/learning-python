# -*- coding: utf-8 -*-
"""
按月分组mail文件
"""
import os
import email
from datetime import datetime
import shutil


# 读取并输出邮件
def read_mail(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fp:
            for line in fp:
                print(line)
    else:
        print("not found file")


# 返回messages对象
def get_message(filepath):
    if os.path.exists(filepath):
        with open(filepath, encoding="utf8", errors='ignore') as fp:
            return email.message_from_file(fp)
    else:
        print("not found file")


def get_date(msg):
    if msg != None:
        return msg.get('date')
    else:
        print('empty object')


if __name__ == "__main__":
    root_dir = r'f:\mail'
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            # 文件全路径
            mail_file_path = os.path.join(root, filename)
            print(mail_file_path)
            # 返回message对象
            msg = get_message(mail_file_path)
            datestring = get_date(msg)
            print("datestring=" + datestring)
            # 没有逗号，直接跳过
            if ',' not in datestring:
                print(", not in datestting")
                continue
            else:
                print(",in the datestring")

            print(' '.join((datestring.split(',')[1]).lstrip().split()[0:3]))
            # Wed, 5 Nov 2014 16:12:05 +0800
            # mail_date=datetime.strptime(datestring[5:24],'%d %b %Y %H:%M:%S')
            mail_date = datetime.strptime(' '.join((datestring.split(',')[1]).lstrip().split()[0:3]), '%d %b %Y')
            mail_month = str(mail_date)[:7]
            print(mail_month)

            if not os.path.exists("e:\\" + mail_month):
                os.mkdir("e:\\" + mail_month)
            else:
                print("e:\\" + mail_month)

                shutil.move(mail_file_path, "e:\\" + mail_month)
