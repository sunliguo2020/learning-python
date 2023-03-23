import requests
import json

def weather_report(city,low_temperature,highest_temperature,weather):
    '''输出天气'''
    output = '''
    {0}今日天气
    最低气温：{1}
    最高气温：{2}
    {3}
    '''
    print(output.format(city,low_temperature,highest_temperature,weather))

url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
response = requests.get(url)
response.encoding = "utf-8"

# 方式1：将JSON字符串转化为字典
weatherinfo = response.text      # JSON类型数据
data = json.loads(weatherinfo)   # 转化为字符串类型
info = data['weatherinfo']
weather_report(info['city'],info['temp1'],info['temp2'],info['weather'])

# 方式2：直接返回字典类型
weatherinfo = response.json()
info = weatherinfo['weatherinfo']
weather_report(info['city'],info['temp1'],info['temp2'],info['weather'])





