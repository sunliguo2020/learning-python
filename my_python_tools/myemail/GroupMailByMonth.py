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

    root_dir = r'F:\email'
    new_email_dir = r'F:\eml_new'

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for filename in files:
            # 源mail文件路径
            mail_file_path = os.path.join(root, filename)
            print(mail_file_path)
            # 返回message对象
            msg = get_message(mail_file_path)
            datestring = get_date(msg)
            if datestring is None:
                continue

            print("datestring=" + datestring)

            # 没有逗号，直接跳过
            if ',' not in datestring:
                print(", not in datestting")
                continue
            else:
                print(",in the datestring")

            # print(' '.join((datestring.split(',')[1]).lstrip().split()[0:3]))
            # Wed, 5 Nov 2014 16:12:05 +0800
            # mail_date=datetime.strptime(datestring[5:24],'%d %b %Y %H:%M:%S')
            mail_date = datetime.strptime(' '.join((datestring.split(',')[1]).lstrip().split()[0:3]), '%d %b %Y')
            mail_month = str(mail_date)[:7]
            mail_day = str(mail_date)[:10]

            print(f"这个文件{filename},日期时间：{mail_date}年月份为：{mail_month},日为{mail_day}")

            # 最后文件路径为 年份-月份/年-月-日 的形式。例如：2016-07/2016-07-06
            new_email_moth_day_dir = os.path.join(new_email_dir, mail_month, mail_day)

            if not os.path.exists(new_email_moth_day_dir):
                os.makedirs(new_email_moth_day_dir)

            print(f"新目录为：{new_email_moth_day_dir}")

            # 文件已经存在则删除
            if os.path.isfile(os.path.join(new_email_moth_day_dir,filename)):
                print(f'{filename}已经存在!准备删除！')
                os.remove(mail_file_path)
            else:
                try:
                    shutil.move(mail_file_path, new_email_moth_day_dir)
                except Exception as e:
                    print(f"移动过程中出错,{e}")
