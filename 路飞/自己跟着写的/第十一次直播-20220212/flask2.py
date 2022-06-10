# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/17 12:18
"""
# 安装flask模块:pip install flask

from time import sleep

from flask import Flask, render_template

# 1.实例化app对象
app = Flask(__name__)


# 装饰器中的参数就是路由地址
@app.route('/main')
def main():  # 视图函数
    sleep(2)
    return 'i am main'


# 一旦启动了服务器后，在浏览器中访问路由地址，在服务器端就会执行视图函数
@app.route('/bobo')
def index1():
    sleep(2)
    return render_template('test.html')


@app.route('/jay')
def index2():
    sleep(2)
    return render_template('test.html')


@app.route('/tom')
def index3():
    sleep(2)
    return render_template('test.html')


if __name__ == "__main__":
    app.run()
