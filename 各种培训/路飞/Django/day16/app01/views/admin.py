# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:40
"""
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pageination import Pagination
from app01.utils.form import AdminModelForm, AdminEditModelForm


def admin_list(request):
    """管理员列表"""
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")

    if search_data:
        # 查询条件
        data_dict['username__contains'] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "pagestring": page_object.html(),
        "search_data": search_data,
    }

    return render(request, "admin_list.html", context)


def admin_add(request):
    """添加管理员"""
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list")
    return render(request, "change.html", {"form": form, "title": title})


def admin_edit(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"error_msg": "此管理员不存在!"})

    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)

        return render(request, "change.html", {"title": title, "form": form})
    form = AdminEditModelForm(instance=row_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, "change.html", {"title": title, "form": form})