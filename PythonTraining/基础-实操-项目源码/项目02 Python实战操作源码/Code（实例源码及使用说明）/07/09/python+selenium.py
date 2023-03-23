# *_* coding : UTF-8 *_*
# 文件名称   ：python+selenium.py
# 开发工具   ：PyCharm
from selenium import webdriver   # 导入浏览器驱动模块
from bs4 import BeautifulSoup    # 导入解析HTML代码模块


url = 'https://www.baidu.com/'
try:
        # 浏览器驱动参数对象
        chrome_options = webdriver.ChromeOptions()
        # 不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 加载谷歌浏览器驱动
        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path='G:/Python/Python37/chromedriver')
        driver.get(url)           # 发送网络请求
        html = driver.page_source  # 获取页面html源代码
        html = BeautifulSoup(html, "html.parser")  # 解析html代码
        # 打印HTML代码中的关键代码
        print('获取关键代码为：\n',html.find('div',class_='qrcode-text'))
        driver.quit()                              # 退出浏览器驱动

except Exception as e:
    print('异常信息为：',e)