# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-06-03 7:47
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


app.run()
