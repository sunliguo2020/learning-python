# *_* coding : UTF-8 *_*
# 文件名称   ：detection_agent.py
# 开发工具   ：PyCharm
import requests  # 导入网络请求模块
import pandas    # 导入pandas模块
import re        # 导入正则表达式模块


ip_table = pandas.read_excel('ip.xlsx')  # 读取代理IP文件内容
ip = ip_table['ip']                      # 获取代理ip列信息
# 头部信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 循环遍历代理IP并通过代理发送网络请求
for i in ip:
    proxies = {'http': 'http://{ip}'.format(ip=i),
               'https': 'http://{ip}'.format(ip=i)}
    try:
        # verify=False不验证服务器的SSL证书
        response = requests.get('http://2019.ip138.com/ic.asp',
                                headers=headers,proxies=proxies,verify=False,timeout=5)
        if response.status_code==200:   # 判断请求是否成功,请求成功说明代理IP可用
            response.encoding='gbk'     # 进行编码
            info = re.findall('<center>(.*?)</center>',response.text)  #  正则匹配代理IP信息
            print(info)                 # 输出当前ip匿名信息
    except Exception as e:
        pass
        # print('错误异常信息为：',e)    # 打印异常信息