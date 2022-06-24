import os
import urllib.request

filename = './1.csv'

with open(filename,encoding='UTF-8') as f:
    lines = f.readlines()
    for i in lines:
        line = i.split(',')
        #print(line)
        filename = line[0]
        pic_url = line[1]
        #创建目录
        if not os.path.exists('./'+filename):
            os.mkdir('./'+filename)
        print(filename)
        for j in pic_url.split(';'):
            print(j)
            #获取url中图片名字
            pic_name = j.split('/')[-1]
            #print(pic_name)
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = { 'User-Agent' : user_agent }
            #urllib.request.urlretrieve(j,'./'+filename+'/'+pic_name)
            pic = urllib.request.urlopen(j)
            #with open('./'+filename+'/'+pic_name,"wb") as picf:
             #   picf.write(pic.read())
    
    