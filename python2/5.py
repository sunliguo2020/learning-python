#!/usr/bin/python

import time

x=0
for i in range(1,101):
    x+=i
print 'x=',x

d = {1:111,2:222,3:333,4:444}

for i in d:
    print d[i]
else:
    print "ending"

#print d.items()

for k,v in d.items():
#    print k
    print v
else:
    print "ending"

for x in range(20):
    print x
    time.sleep(1)
else:
    print "ending"
