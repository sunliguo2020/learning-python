from itsdangerous import TimedJSONWebSignatureSerializer as TJSS
from itsdangerous import SignatureExpired

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views.generic import View

from django.conf import settings
from apps.mail.models import User
from celery_execute_task.sendmail import send_activate_email
# Create your views here.


class VerifyMail(View):
    """邮件验证功能"""

    def get(self, request):
        """页面显示"""

        return render(request, 'register.html')

    def post(self, request):
        """业务处理"""

        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # 校验数据
        if not all([username, password, phone, email]):
            # 缺少相关数据
            return HttpResponse('校验数据失败')

        user = User.objects.create_user(username, email, password, phone=phone)

        # 正式处理发送邮件
        # 加密用户的身份信息，生成激活token
        serializer = TJSS(settings.SECRET_KEY, 900)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        # 默认解码为utf8
        token = token.decode()

        # 使用celery发邮件
        send_activate_email.delay(email, username, token)

        return HttpResponse('注册成功，请注意查收激活账户邮件')


class UserActivate(View):
    """用户通过邮件激活功能"""

    def get(self, request, token):
        """点击邮件链接激活业务处理"""

        serializer = TJSS(settings.SECRET_KEY, 900)
        try:
            info = serializer.loads(token)

            # 获取要激活用户的id
            user_id = info['confirm']

            # 根据id获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 跳转到登录页面
            return HttpResponse('用户已成功激活！')

        except SignatureExpired as se:
            # 激活链接已过期，应重发激活邮件
            return HttpResponse('激活链接已过期！')
