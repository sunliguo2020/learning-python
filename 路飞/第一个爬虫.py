
import urllib.request

print(type(urllib.request))
print(dir(urllib))
req = urllib.request.Request("http://www.baidu.com")
print(urllib.request.urlopen(req).read())


