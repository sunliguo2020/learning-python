"""
用Python代码快速创建一个网站，接收APP发送来的请求
安装：
    pip install flask
"""
import json
from flask import Flask, request

app = Flask(__name__)


# http://192.168.0.6:9999/login
@app.route('/login', methods=['POST'])
def login():
    # 接收其他人发送来的请求的数据
    print(request.form.to_dict())

    # 1.校验签名md5

    # 2.数据库校验用户名密码是否正确

    # 直接认为登录成功，返回登录成功后的数据
    return json.dumps({"status": True, "token": "fffk91234ksdujsdsd", "name": "武沛齐"}, ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
