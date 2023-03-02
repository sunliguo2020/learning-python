import urllib2
import os
#文件上一次保存日期：2016/8/9 15:17

def get_page(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
    content = urllib2.urlopen(req).read()
    a = content.find("current-comment-page")+23
    b = content.find(']',a)
    return content[a:b]

def save_imgs(floder,img_addrs):
    pass

def find_imgs(url):
	pass
def download_mm(floder="./mm",pages=10):
	os.mkdir(floder)
	os.chdir(floder)

	url = "http://jandan.net/ooxx"
	page_num  = int(get_page(url))

	for i in xrange(pages):
		pages -= 1

		page_url = url + "page-"+pages+"#comments"
		img_addrs = find_imgs(page_url)
		save_imgs(floder,img_addrs)


if __name__ == "__main__":
    download_mm()