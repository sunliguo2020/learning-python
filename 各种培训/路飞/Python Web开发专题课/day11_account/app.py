# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/8 8:48
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/do/register', methods=['GET'])
def do_register():
    # request.form
    return request.args


if __name__ == '__main__':
    app.run()
