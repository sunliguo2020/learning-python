# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/7 21:50
"""
from flask import Flask

app = Flask(__name__)


@app.route('/show/info')
def index():
    return "中国联通"


if __name__ == '__main__':
    app.run()
