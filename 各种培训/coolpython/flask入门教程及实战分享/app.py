# -*- coding: utf-8 -*-
'''
 @Time : 2022/7/3 17:55
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 @File : app.py
 @Project : github
'''
from flask import Flask,request

print(__name__)
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World!"

@app.route('/books')
def books():
    return "books"

@app.route('/users',methods=['GET','POST'])
def users():
    if request.method == 'GET':
        return 'get'
    if request.method == 'POST':
        return 'POST'
    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)
