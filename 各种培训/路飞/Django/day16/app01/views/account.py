# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 16:55
"""
from django.shortcuts import render, redirect, HttpResponse
from app01.utils.form import LoginForm
from app01 import models
from app01.utils.code import check_code
from io import BytesIO


def login(request):
    """登录"""
    if request.method == 'GET':
        # 判断已经登陆过，就直接进入
        if request.session.get('info'):
            return redirect('/admin/list/')
        # 没有登陆过
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        # {'username':'','password':'','code':''}
        # print(form.cleaned_data)
        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {"form": form})

        # 去数据库校验
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；再写入到sessions中;
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/admin/list')

    return render(request, 'login.html', {"form": form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    """生成图片验证码"""
    img, code_string = check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给session设置60秒超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())
