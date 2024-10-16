# -*- coding: utf-8 -*-
"""
 @Time : 2024/9/22 11:05
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from flask import Flask, render_template

app = Flask('ss')


@app.route('/show/info')
def index():
    """
    """
    # return "中国联通"
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
