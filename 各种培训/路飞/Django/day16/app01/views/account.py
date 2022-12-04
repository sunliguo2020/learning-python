# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 16:55
"""
from django.shortcuts import render, redirect
from app01.utils.form import LoginForm
from app01 import models


def login(request):
    """登录"""
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        print(form.cleaned_data)
        # 去数据库校验
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；再写入到sessions中;
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect('/admin/list')

    return render(request, 'login.html', {"form": form})

def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')
