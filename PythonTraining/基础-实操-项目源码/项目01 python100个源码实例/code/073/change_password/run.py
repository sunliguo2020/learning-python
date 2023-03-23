from flask import Flask,render_template, redirect, url_for,flash
from app.forms import SettingForm
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin,LoginManager,current_user,login_required
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


@app.route('/change_password',methods=['GET','POST'])
@login_required
def change_password():
    form = SettingForm()
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.password.data):
            # 根据当前用户id获取用户信息
            user = User.query.filter_by(id=current_user.id).first()
            # 获取新密码
            new_password = form.new_password.data
            # 对新密码加密
            user.password = generate_password_hash(new_password)
            # 提交到数据库
            db.session.commit()
            # 将成功消息存入闪存
            flash('修改成功', 'success')
            # 保存成功后，跳转到登录页面
            return redirect(url_for('change_password'))
        else:
            # 将失败消息存入闪存
            flash('原始密码错误', 'danger')
    return render_template('change_password.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)





