from app import app, db
from app.models import User,Log
from flask import render_template, request, redirect, url_for,flash
from app.forms import LoginForm,SettingForm,InfoForm
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user,logout_user,login_required,current_user
import json
from .utils import get_working_age,get_check_users,get_uncheck_users
from functools import wraps

def is_admin(f):
    """
    管理员权限检测
    :param f:
    :return:
    """
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if current_user.is_admin != 1:
            flash('非管理员账户无权访问', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login',methods=['GET','POST'])
def login():
    """
    判断用户是否登录
    :return:
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() # 实例化LoginForm()类
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('用户名和密码不匹配', 'danger')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    """
    退出登录
    :return:
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/account',methods=['GET','POST'])
@login_required
def account():
    """
    修改密码
    :return:
    """
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
            return redirect(url_for('account'))
        else:
            # 将失败消息存入闪存
            flash('原始密码错误', 'danger')
    return render_template('account.html',form=form)

@app.route('/')
@app.route('/info')
@login_required
def index():
    """
    显示登录用户的信息
    :return:
    """
    # 获取用户信息
    user = User.query.filter_by(id=current_user.id).first()
    working_age = get_working_age(user.hiredate)
    # 渲染模板
    return render_template('info.html',user=user,working_age=working_age)

@app.route('/edit')
@login_required
def edit():
    """
    编辑用户信息
    :return:
    """
    # 获取用户信息
    form = InfoForm()
    user = User.query.filter_by(id=current_user.id).first()
    return render_template('edit.html',user=user,form=form)

@app.route('/update',methods=['POST'])
@login_required
def update():
    """
    更改用户信息
    :return:
    """
    # 获取用户信息
    user = User.query.filter_by(id=current_user.id).first()
    form = InfoForm()
    if form.validate_on_submit():
        content = {}
        content['username']    =  f'{user.username  },{request.form["username"]  }'
        content['department']  =  f'{user.department},{request.form["department"]}'
        content['position']    =  f'{user.position  },{request.form["position"]  }'
        content['hiredate']    =  f'{user.hiredate  },{request.form["hiredate"]  }'

        user.username   = request.form['username']
        user.department = request.form['department']
        user.position   = request.form['position']
        user.hiredate   = request.form['hiredate']

        log = Log()
        log.user_id = current_user.id
        log.update_content = json.dumps(content)
        try:
            db.session.add(log)
            db.session.commit()
        except:
            db.session.rollback()  # 事务回滚
        # 将成功消息存入闪存
        flash('修改成功', 'success')
        # 保存成功后，跳转到登录页面
        return redirect(url_for('index'))
    return render_template('edit.html',form=form,user=user)

@app.route('/list/type/<type>')
@login_required
@is_admin
def list(type):
    """
    审核和待审核列表
    :param type:
    :return:
    """
    data = []
    if type == "uncheck":
        users = User.query.filter_by(status=0).all()
        data = get_uncheck_users(users)
    else:
        users = User.query.filter_by(status=1).all()
        data = get_check_users(users)
    return render_template('list.html',data=data)

@app.route("/update_status/<int:id>/type/<type>")
@login_required
def update_status(id,type):
    """
    更改审核状态
    :param id:   用户id
    :param type: 状态类型，uncked:未审核，checked: 审核通过
    :return:
    """
    # 员工只能更改自己审核状态,管理员可以更改所有员工审核状态
    if current_user.id != id and current_user.is_admin != 1:
        flash('没有修改权限',category='danger')
        redirect(url_for('index'))

    user = User.query.filter_by(id=id).first()
    if type == 'uncheck':
        user.status = 0
        db.session.commit()
        # 保存成功后，跳转到登录页面
        return redirect(url_for('list',type='uncheck'))
    elif type == 'checked':
        user.status = 1
        db.session.commit()
        # 如果是管理员账号，跳转到审核通过页面
        # 如果是员工账号，跳转到个人信息页面
        if current_user.is_admin:
            return redirect(url_for('list',type='checked'))
        else:
            return redirect(url_for('index'))
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_note_found(e):
    return render_template('404.html'),404

