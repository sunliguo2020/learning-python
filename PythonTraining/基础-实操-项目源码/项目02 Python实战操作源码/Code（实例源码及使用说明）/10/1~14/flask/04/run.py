from flask import Flask ,request ,render_template,redirect
from forms import RegistrationForm

app = Flask(__name__)     # 实例化Flask类
app.secret_key = "mrsoft" # 设置secret_key

@app.route("/")
def index():
    '''首页'''
    return "Welcome to Flask"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form) # 实例化RegistrationForm类
    if request.method == 'POST' and form.validate(): # 判断是否提交表单，并且表单字段验证通过
        pass # 省略注册逻辑
        return redirect('/')
    return render_template('register.html', form=form) # 渲染模板

if __name__ == "__main__":
    app.run(debug=True) # 开启调试模式
