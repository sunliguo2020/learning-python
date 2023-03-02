from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import User
import hashlib


# Create your views here.
class Message(View):
    def get(self, request):
        print(dir(request))
        name = request.GET.get('name')
        age = request.GET.get('age')


def reg_view(request):
    # 注册
    # GET 返回页面
    # POST 处理数据

    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == "POST":

        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # 1. 两次密码是否一致
        if password2 != password1:
            return HttpResponse('两次密码输入不一致')

        m = hashlib.md5()
        m.update(password1.encode())
        password_m = m.hexdigest()

        # 2、当前用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已注册')
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('---create user error %s' % (e))
            return HttpResponse('用户已注册')

        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponse('注册成功')


def login_view(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        passwrord = request.POST.get('password', '')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('')
            return render(request, '用户名或者密码错误！')

        m = hashlib.md5()
        m.update(passwrord.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('用户名或者密码错误')

        # 记录会话状态
        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponse("登录成功")
