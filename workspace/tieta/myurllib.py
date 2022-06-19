import urllib
import urllib.request
import pysnmp
import os


os.system("dir")


f = urllib.request.urlopen("http://www.baidu.com")
print(f.read().decode("utf-8"))