# *_* coding : UTF-8 *_*

# 文件名称   ：demo03.py
# 开发工具   ：PyCharm
city=['上海', '广州', '上海', '成都', '上海', '上海', '北京', '上海', '广州', '北京', '上海']

ncitx=list(set(city))
ncitx.sort( key=city.index)
print(ncitx)
