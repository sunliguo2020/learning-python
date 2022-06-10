#!/usr/bin/python
import email
import os
from datetime import datetime

# mail path
PATH = ""


def read_mail(path):
    if os.path.exists(path) and path.endswith('.eml'):
        with open(path) as fp:
            for line in fp:
                print(line)
    else:
        not_find_file()


def open_file(path):
    if os.path.exists(path):
        return open(path, 'r')
    else:
        not_find_file()


def get_message(path):
    if os.path.exists(path) and path.endswith('.eml'):
        fp = open_file(path)
        return email.message_from_file(fp)
    else:
        not_find_file()


def get_date(msg):
    if msg != None:
        # return email.utils.parseaddr(msg.get('date'))
        return msg.get('date')
    else:
        empty_obj()


def not_find_file():
    print("Not find file!")


def empty_obj():
    print('msg is empty')


if __name__ == "__main__":
    for root, dirs, files in os.walk('./eml'):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            msg = get_message(file_path)
            # print(msg)
            datestring = get_date(msg)
            if datestring != None:
                date = datetime.strptime(datestring[5:24], '%d %b %Y %H:%M:%S')
                mail_day = str(date.year) + '-' + str(date.month) + '-' + str(date.day)

                print(mail_day)
        # if not os.path.exists(mail_day):
        # 	os.mkdir(mail_day)
