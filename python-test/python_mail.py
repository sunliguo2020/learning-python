#!/usr/bin/python
import os
import email
from datetime import datetime

#mail path
PATH=""

def read_mail(path):
	if os.path.exists(path):
		with open(path) as fp:
			for line in fp:
				print(line)
	else:
		not_find_file()

def open_file(path):
	if os.path.exists(path):
		return open(path,'r')
	else:
		not_find_file()
	
def get_message(path):
	if os.path.exists(path):
		fp=open_file(path)
		return email.message_from_file(fp)
	else:
		not_find_file()

def get_date(msg):
	if msg != None:
		#return email.utils.parseaddr(msg.get('date'))
		return msg.get('date')
	else:
		empty_obj()
	
def not_find_file():
	print("Not find file!")
def empty_obj():
	print('msg is empty')

if __name__ == "__main__":
	msg=get_message('./1.eml')
	datestring=get_date(msg)
	date=datetime.strptime(datestring[5:24],'%d %b %Y %H:%M:%S')
	mail_day=str(date.year)+'-'+str(date.month)+'-'+str(date.day)
	if not os.path.exists(mail_day):
		os.mkdir(mail_day)

