# *_* coding : UTF-8 *_*

# 文件名称   ：demo04.py
# 开发工具   ：PyCharm
city=['上海', '广州', '上海', '成都', '上海', '上海', '北京', '上海', '广州', '北京', '上海']
city.sort()
for x in city:
     while city.count(x)>1:
         del city[city.index(x)]

print(city)
