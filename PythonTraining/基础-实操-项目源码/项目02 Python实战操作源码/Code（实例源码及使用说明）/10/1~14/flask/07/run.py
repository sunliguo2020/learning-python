from flask import Flask ,request ,render_template ,session ,redirect,url_for
from functools import wraps

app = Flask(__name__)     # 实例化Flask类
app.secret_key = "mrsoft" # 设置secret_key

def user_login(f):
    '''登录装饰器'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:           # 如果Session中不存在user_id，那么跳转到登录页
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''登录页'''
    if request.method == 'POST':
        session["user_id"] = 1                # 将user_id写入Session
        session["username"] = request.form.get('username','',type=str)  # 将username写入Session
        return redirect(url_for("homepage"))  # 登录成功，跳转到个人主页
    return render_template('login.html')      # 渲染模板

@app.route("/logout/")
def logout():
    """
    退出登录
    """
    session.pop("user_id", None)        # 清除Session
    session.pop("username", None)       # 清除Session
    return redirect(url_for('login'))   # 重定向到home模块下的登录。

@app.route('/homepage')
@user_login
def homepage():
    '''个人主页'''
    return render_template('homepage.html') # 渲染模板

app.run(debug=True) # 开启调试模式
