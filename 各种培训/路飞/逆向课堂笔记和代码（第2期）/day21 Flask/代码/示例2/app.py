import os
from flask import Flask, request, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


def check_is_valid(token):
    db_path = os.path.join(BASE_DIR, 'db.csv')
    with open(db_path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.split(",")[0] == token:
                return True


@app.route("/vip")
def vip():
    # 接收从URL中传递过来的值 & 判断是否有
    token = request.args.get("token")
    if not token:
        return "无权访问"

    # 判断token的合法性
    if not check_is_valid(token):
        return "无权访问"

    # 提供信息
    # return "<h1 style='color:red;'>你好呀</h1>"
    return render_template("vip.html", xx=token)


@app.route("/check", methods=["POST"])
def check():
    # 1.去URL中获取token
    token = request.args.get('token')
    if not check_is_valid(token):
        return "无权访问"

    # 2.去请求体中获取 n1 / n2
    phone = request.form.get("n1")
    code = request.form.get("n2")

    # 拿着手机号和验证码就去做mt操作
    return "成功"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
