import urllib2

req  = urllib2.Request(url = "http://www.baidu.com",
	data = "THis data is passed to stdin of the CGI")

req.add_header("user-agent","Firefox")
req.add_header("test","sunliguo")

f = urllib2.urlopen(req)

print f.read()