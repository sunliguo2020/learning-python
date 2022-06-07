#!/usr/bin/python
import os

for i in os.walk('/boot'):
	for j in i[2]:
		print os.path.join(i[0],j)
