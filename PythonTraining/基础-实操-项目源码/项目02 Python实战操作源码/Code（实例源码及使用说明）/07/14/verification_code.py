# *_* coding : UTF-8 *_*
# 文件名称   ：verification_code.py
# 开发工具   ：PyCharm

from selenium import webdriver  # 导入浏览器驱动模块

# 加载谷歌浏览器驱动
driver = webdriver.Chrome(executable_path='G:/Python/Python37/chromedriver')
# 浏览器窗口全屏显示
driver.maximize_window()
# 发送网络请求，实现浏览器打开页面
driver.get('http://my.cnki.net/elibregister/commonRegister.aspx')
# 获取网页中验证码html代码标签
dynamic = driver.find_element_by_class_name('dynamic-pic')
dynamic.screenshot('C:/Users/Administrator/Desktop/code.png')  # 对验证码进行截屏,并保存在指定目录下
driver.close()    # 关闭浏览器窗口