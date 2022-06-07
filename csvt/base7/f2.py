#!/usr/bin/env python
# -*- coding:utf8 -*-
x = input("input x:")
msg = ''
if x >= 90:
    msg = u'优秀'
elif x >= 80:
    msg = u"良"
elif x >= 60:
    msg = u"中"
else :
    msg= u'差'

print msg
