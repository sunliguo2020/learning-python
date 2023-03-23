# *_* coding : UTF-8 *_*
# 文件名称   ：GitHub_Login.py
# 开发工具   ：PyCharm

import requests  # 导入网络请求模块
from lxml import etree  # 导入lxml模块


class GitHub_Login():
    def __init__(self, username, password):
        # 头部信息
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/57.0.2987.133 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }

        self.login_url = 'https://github.com/login'  # 登陆页面地址
        self.post_url = 'https://github.com/session'  # 实现登陆的请求地址
        self.session = requests.Session()  # 创建Session会话对象

        self.user_name = username  # 用户名
        self.password = password  # 密码

    # 获取authenticity_token信息
    def get_token(self):
        # 发送登陆页面的网络请求
        response = self.session.get(self.login_url, headers=self.headers)
        html = etree.HTML(response.text)  # 解析html
        # 提取authenticity_token信息
        token = html.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        return token  # 返回信息

    # 实现登陆
    def login(self):
        # 请求参数
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': self.user_name,
            'password': self.password,
            'webauthn - support': 'supported'
        }
        # 发送登录请求
        response = self.session.post(self.post_url,
                                     headers=self.headers, data=post_data)
        if response.status_code == 200:  # 判断请求成功
            html = etree.HTML(response.text)  # 解析html
            # 获取注册号码
            register_number = html.xpath('/html/body/div[1]/header/'
                                         'div[8]/details/details-menu/div[1]/a/strong')[0]
            print('注册号码为：', register_number.text)  # 打印登录后获取的注册号码
        else:
            print('登录失败！')


if __name__ == '__main__':
    user_name = input('请输入您的用户名： ')  # 获取输入的账号
    password = input('请输入您的密码： ')  # 获取输入的密码
    login = GitHub_Login(user_name, password)  # 创建登录类对象并传递输入的账号与密码
    login.login()  # 调用登录方法
