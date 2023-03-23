import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# 配置邮箱服务器信息
mail_host = "smtp.qq.com"   # 设置服务器
mail_user = "694798056"     # 用户名
mail_pass = "gfgwmfbzmutebajc"  # 口令

# 配置发件人、收件人信息
sender = '694798056@qq.com' # 发件人邮箱
receivers = ['694798056@qq.com']  # 接收邮件，可设置为多个邮箱


def message_config():
    """
    配置邮件信息
    :return: 消息对象
    """
    # 第三方 SMTP 服务
    content = MIMEText('Python课程数据,注意查收')
    message = MIMEMultipart() # 多个MIME对象
    message.attach(content)  # 添加内容
    message['From'] = Header("Andy", 'utf-8') # 发件人
    message['To']   = Header("老冯", 'utf-8')  # 收件人
    message['Subject'] = Header('Python课程数据', 'utf-8') # 主题
    # 添加Excel类型附件
    file_name = 'Python课程数据2019-12-31.xlsx' # 文件名
    file_path = os.path.join(file_name)        # 文件路径
    xlsx = MIMEApplication(open(file_path, 'rb').read())  # 打开Excel,读取Excel文件
    xlsx["Content-Type"] = 'application/octet-stream'     # 设置内容类型
    xlsx.add_header('Content-Disposition', 'attachment', filename=file_name) # 添加到header信息
    message.attach(xlsx)
    return message

def send_mail(message):
    """
    发送邮件
    :param message: 消息对象
    :return: None
    """
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host) # 使用SSL连接邮箱服务器
        smtpObj.login(mail_user, mail_pass)   # 登录服务器
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
        print("邮件发送成功")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("开始执行")
    message = message_config() # 调用配置方法
    send_mail(message)         # 发送邮件
    print("执行结束")
