from flask import Flask, request,render_template,redirect
from flask_mail import Mail, Message
from threading import Thread
from forms import RegistrationForm

app = Flask(__name__)

# 配置邮件服务
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '#####'  # 邮箱
app.config['MAIL_PASSWORD'] = '******' # 验证密保
mail = Mail(app)

def send_async_email(app, msg):
    '''异步发送邮件'''
    with app.app_context():
        mail.send(msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form) # 实例化RegistrationForm类
    if request.method == 'POST' and form.validate(): # 判断是否提交表单，并且表单字段验证通过
        username = request.form.get('username','尊敬的用户') # 获取用户名
        email = request.form.get('email')   # 获取邮箱
        recipients = list() # 收件人邮件列表
        recipients.append(email) # 加入收件人邮件列表
        msg = Message('[明日学院]网站用户激活邮件', sender='694798056@qq.com', recipients=recipients)
        msg.body = '您好'+username+'，明日学院管理员想邀请您激活您的用户，点击链接激活。https://www.mingrisoft.com'
        # 使用线程
        thread = Thread(target=send_async_email, args=[app, msg]) # 创建线程实例
        thread.start() # 开启线程
        return redirect('/mail_success') # 跳转路由
    return render_template('register.html', form=form) # 渲染模板

@app.route("/mail_success")
def mail_success():
    return "邮件发送成功"

if __name__ == '__main__':
    app.run(debug=True)