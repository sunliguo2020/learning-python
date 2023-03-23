# *_* coding : UTF-8 *_*
# 文件名称   ：selenium_toggle_pages.py
# 开发工具   ：PyCharm

from selenium import webdriver  # 导入浏览器驱动模块
import time                      # 导入时间模块
class Selenium():                # 创建selenium类
    def __init__(self):
        # 加载谷歌浏览器驱动
        self.driver = webdriver.Chrome(
            executable_path='G:/Python/Python37/chromedriver')
        self.driver.maximize_window()  # 浏览器窗口最大化
        self.driver.get('https://www.taobao.com/') # 打开淘宝官网
    # 切换页面
    def toggle_pages(self,url):
        time.sleep(3)    # 等待2秒
        js = 'window.open("{url}")'.format(url=url)  # 通过执行js，开启一个天猫的窗口
        self.driver.execute_script(js)
        # 当前窗口的handle，也就是淘宝窗口
        taobao_handle = self.driver.current_window_handle
        # 获取所有窗口句柄集合（列表类型）
        handles = self.driver.window_handles
        # 获取天猫窗口
        new_handle = None
        for handle in handles:
            if handle != taobao_handle:
                new_handle = handle
        time.sleep(3)
        # 切换淘宝窗口，并传递执行权力
        self.driver.switch_to.window(taobao_handle)
        time.sleep(3)
        self.driver.close()  # 关闭淘宝窗口
        # 切换天猫窗口，并传递执行权力
        self.driver.switch_to.window(new_handle)
        time.sleep(3)
        self.driver.close()  # 关闭天猫窗口
if __name__ == '__main__':
    selenium = Selenium()   #  创建Selenium对象
    selenium.toggle_pages('https://www.tmall.com/') # 切换天猫官网

