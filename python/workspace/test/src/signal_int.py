#conding:utf-8

import signal,os
from time import sleep 

def sinint_handler(signum,frame):
	print "catched interrupt signal"
	exit(-1)

signal.signal(signal.SIGINT,sinint_handler)
#signal.signal(signal.SIGTERM,sinint_handler)

while True:
	print "pid = %s" % os.getpid()
	#sleep(2)