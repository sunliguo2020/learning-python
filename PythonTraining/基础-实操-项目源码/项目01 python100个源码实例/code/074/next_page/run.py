from flask import Flask,render_template, request, redirect, url_for,flash
from app.forms import LoginForm,SettingForm
from werkzeug.security import check_password_hash
from werkzeug.urls import url_parse
from flask_login import UserMixin,LoginManager,login_user,logout_user,current_user,login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 基本配置
app.config["SECRET_KEY"] = "mrsoft"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://root:root@localhost/flask'
        )

# 实例化SQLAlchemy类
db = SQLAlchemy(app)
# 实例化LoginManager类
login_manager = LoginManager(app)
# 跳转的页面
login_manager.login_view = 'login'
# 提示信息
login_manager.login_message = "请先登录"
# 提示样式
login_manager.login_message_category = 'danger'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(125), nullable=False)
    password = db.Column(db.String(125), nullable=False)

@app.route('/login',methods=['GET','POST'])
def login():
    """
    登录
    """
    # 如果用户已经登录，访问登录页面会跳转到首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() # 实例化LoginForm()类
    # 验证表单
    if form.validate_on_submit():
        # 判断邮箱是否存在,如果不存在提示错误信息，
        # 如果存在，继续判断邮箱密码是否匹配
        # 如果匹配，跳转到上一页或首页，否则，提示错误信息
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('邮箱不存在', 'danger')
        elif check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('用户名和密码不匹配', 'danger')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    """
    退出登录
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():
    """
    首页
    """
    return render_template("index.html")

@app.route('/change_password')
@login_required
def change_password():
    """
    密码
    """
    form = SettingForm()
    return render_template("change_password.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)





