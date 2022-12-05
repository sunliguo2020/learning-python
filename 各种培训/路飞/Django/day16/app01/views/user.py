# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:01
"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pageination import Pagination
from app01.utils.form import UserModelForm


def user_list(request):
    """用户管理"""

    query_set = models.UserInfo.objects.all()
    page_object = Pagination(request, query_set, page_size=2)
    context = {
        "user_list": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'user_list.html', context)


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        content = {
            "gender_choice": models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all(),
        }

        return render(request, 'user_add.html', content)
    # 获取用户提交的数据
    name = request.POST.get('name')
    age = request.POST.get('age')
    pwd = request.POST.get('pwd')
    ac = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gd = request.POST.get('gd')
    dp = request.POST.get('dp')
    # 添加到数据库中
    models.UserInfo.objects.create(name=name,
                                   password=pwd,
                                   age=age,
                                   account=ac,
                                   create_time=ctime,
                                   gender=gd,
                                   dpart_id=dp)
    return redirect('/user/list/')


def user_delete(request, nid):
    """"删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


def user_model_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})
    # 用户POST提交的数据
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    else:  # 校验失败，显示错误信息
        return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_obj)
        return render(request, 'user_edit.html', {"form": form})

    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        # 默认保存的是用户输入的所有的数据，如果想要在用户输入意外增加值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_edit.html', {'form': form})
