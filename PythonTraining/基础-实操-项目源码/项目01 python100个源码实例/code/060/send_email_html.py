import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 配置邮箱服务器信息
mail_host = "smtp.qq.com"   # 设置服务器
mail_user = "694798056"     # 用户名
mail_pass = "gfgwmfbzmutebajc"  # 口令

# 配置发件人、收件人信息
sender = '694798056@qq.com' # 发件人邮箱
receivers = ['694798056@qq.com']  # 接收邮件，可设置为多个邮箱

mail_msg = """
<h2>欢迎来到明日学院</h2>
<p><a href="http://www.mingrisoft.com">明日学院官方网址</a></p>
<a><img src="https://www.mingrisoft.com/Public/images/logo.png"></a>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("明日学院", 'utf-8')
message['To'] = Header("明日学员", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(mail_host)    # 实例化SMTP
    smtpObj.login(mail_user, mail_pass)  # 登录服务器
    smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")