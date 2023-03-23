# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import requests  # 网络请求模块

# 头部信息
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
# 获取商品价格的请求地址
url = 'https://c0.3.cn/stock?skuId=12451724&venderId=1000117165&' \
      'cat=1713,3287,3797&area=1_72_2799_0&buyNum=1&extraParam={%22originid%22:%221%22}' \
      '&ch=1&pduid=1365193482&pdpin=&fqsp=0'
# 发送网络请求
re = requests.get(url,headers = header)
json = re.json()    # 解析json数据
print('当前售价为：',json['stock']['jdPrice']['op'])  # 当前售价
print('定价为：',json['stock']['jdPrice']['m'])   # 定价
print('会员价为：',json['stock']['jdPrice']['tpp']) # 会员价