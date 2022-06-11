import os
import json
import redis
from flask import Flask, request, render_template, redirect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POOL = redis.ConnectionPool(host='124.222.193.204', port=6379, password='foobared', encoding='utf-8',
                            max_connections=1000)

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


@app.route("/vip", methods=['GET', "POST"])
def vip():
    # 判断用户发送的是什么请求？
    if request.method == "GET":
        # 接收从URL中传递过来的值 & 判断是否有
        token = request.args.get("token")
        if not token:
            return "无权访问"

        # 判断token的合法性
        if not check_is_valid(token):
            return "无权访问"

        # 去文件中获取用户所有的数据并展示在页面上
        result_list = []  # [ [邮箱,数量], [邮箱,数量], [邮箱,数量], [邮箱,数量]]
        file_path = os.path.join(BASE_DIR, 'order', "{}.txt".format(token))
        if os.path.exists(file_path):
            with open(file_path, mode='r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    row_list = line.split(",")  # [邮箱,数量]
                    result_list.append(row_list)

        return render_template("vip.html", result_list=result_list)
    else:
        # 1.校验token是否合法
        token = request.args.get("token")
        if not token:
            return "无权访问"
        # 判断token的合法性
        if not check_is_valid(token):
            return "无权访问"

        # 2.写入本地文件
        email = request.form.get("email")
        count = request.form.get("count")
        file_path = os.path.join(BASE_DIR, 'order', "{}.txt".format(token))
        with open(file_path, mode='a', encoding='utf-8') as f:
            f.write(f"{email},{count}\n")

        # 3.订单放到队列，连接redis并写入到redis中。
        #    - 安装并启动redis：Windows（https://pythonav.com/wiki/detail/10/82/）   Linux
        #    - pip install redis
        #    - 基于redis模块实现对redis进行操作 List  ->  lpush     []      rpop
        conn = redis.Redis(connection_pool=POOL)
        conn.lpush("mt_task_queue", json.dumps([email, count]))
        conn.close()

        # 4.给用户返回，做重定向 -> GET请求
        return redirect(f"/vip?token={token}")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
