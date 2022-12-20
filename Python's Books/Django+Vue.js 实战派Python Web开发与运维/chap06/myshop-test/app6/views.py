from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from app6.models import MyUser


# Create your views here.
def user_reg(request):
    if request.method == 'GET':
        return render(request, '6/user_reg.html')
    if request.method == 'POST':
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        re_pwd = request.POST.get('re-password')
        print('uname=', uname)
        if pwd != re_pwd:
            info = '密码和重复密码不一样'
        else:
            if User.objects.filter(username=uname):
                info = '用户已经存在'
            else:
                d = dict(username=uname,
                         password=pwd,
                         email='111@111.com',
                         is_staff=1,
                         is_active=1,
                         is_superuser=1)
                print(d)
                user = User.objects.create_user(**d)
                info = '注册成功，请登录'
        return render(request, '6/user_reg.html', {'info': info})


def user_login(request):
    if request.method == "GET":
        return render(request, '6/user_login.html')
    if request.method == "POST":
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        if User.objects.filter(username=uname):
            # 如果存在用户，则验证
            user = authenticate(username=uname, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    info = '登录成功'
                else:
                    info = '用户未激活'
            else:
                info = '用户名或密码不对'
        else:
            info = '用户账号不存在，请查询'
        return render(request, '6/user_login.html', {"info": info})


def myuser_reg(request):
    if request.method == 'GET':
        return render(request, '6/user_reg.html')
    if request.method == 'POST':
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        if MyUser.objects.filter(username=uname):
            info = '用户已存在'
        else:
            d = dict(username=uname,
                     password=pwd,
                     email='222@123.com',
                     is_staff=1,
                     is_active=1,
                     is_superuser=1,
                     weChat='yangcoder',
                     level='1'
                     )
            user = MyUser.objects.create_user(**d)
            info = '注册成功，请登录'

            return redirect(reverse('app6_myuser_login'))


def myuser_login(request):
    if request.method == 'GET':
        return render(request, '6/user_login.html')
    if request.method == "POST":
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        if MyUser.objects.filter(username=uname):
            user = authenticate(username=uname, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    info = '登录成功'
                    return render(request, '6/user_index.html')
                else:
                    info = '用户未激活'
            else:
                info = '账号密码不对，请重新输入'
            return render(request, '6/user_login.html', {'info': info})
        return render(request, '6/user_login.html', {'info': "找不到该用户"})


def myuser_logout(request):
    logout(request)
    return redirect(reverse('app6_myuser_login'))

@permission_required('app6.view_myuser')
@login_required
def user_index(request):
    users = MyUser.objects.all()
    return render(request, '6/user_index.html', {'users': users})


@permission_required('app6.change_myuser')
@login_required()
def user_edit(request):
    return render(request,'6/user_edit.html')