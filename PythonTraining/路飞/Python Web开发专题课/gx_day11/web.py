# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/7 21:50
"""
from flask import Flask, render_template

app = Flask(__name__)


# print(dir(app))
# for item in app.__dir__():
#     print(app.item)

@app.route('/show/info')
def index():
    # return "中国联通"
    # return "中国<span style:red;>联通</span>"
    # flask 自动打开这个文件，并读取内容，返回用户。
    return render_template('index.html')


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run()
