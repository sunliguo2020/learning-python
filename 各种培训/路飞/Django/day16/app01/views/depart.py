# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:01
"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pageination import Pagination


# Create your views here.

def depart_list(request):
    """部门列表"""
    # 数据库总所有的部门信息
    queryset = models.Department.objects.all()
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, "depart_list.html", context)


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取用户通过post提交的数据
    title = request.POST.get('title')

    # 保存到数据库
    if models.Department.objects.filter(title=title):
        return render(request, 'error.html', {"error_msg": "此部门已经存在!"})
    models.Department.objects.create(title=title)
    # 重定向到部门列表
    return redirect('/depart/list/')


def depart_delete(request):
    """删除部门"""
    # assert isinstance(request.GET.get, object)
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()

        return render(request, 'depart_edit.html', {"row_object": row_object})
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")
