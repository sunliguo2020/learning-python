# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:02
"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pageination import Pagination
from app01.utils.form import MobileEditModelForm, MobileModelForm, ShoujihaoModelsForm, UserModelForm


def prettynum_list(request):
    """靓号显示"""
    # 创建测试数据
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile='15244425554',price=102,level=1,status=1)

    data_dict = {}
    search_data = request.GET.get('q', "")

    if search_data:
        data_dict['mobile__contains'] = search_data

    query_set = models.PrettyNum.objects.filter(**data_dict).order_by("mobile")

    page_object = Pagination(request, query_set, page_size=20)

    context = {
        "num_list": page_object.page_queryset,
        "search_data": search_data,
        "page_string": page_object.html()}

    return render(request, "prettypnum_list.html", context)


def prettynum_add(request):
    """靓号添加"""
    if request.method == "GET":
        form = MobileModelForm()
        return render(request, "prettynum_add.html", {"form": form})
    form = MobileModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    else:
        return render(request, "prettynum_add.html", {"form": form})


def prettynum_edit(request, nid):
    """靓号编辑"""
    row_obj = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = MobileEditModelForm(instance=row_obj)
        return render(request, "prettynum_edit.html", {"form": form})

    form = MobileEditModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/prettynum/list/")

    return render(request, 'prettynum_edit.html', {"form": form})


def prettynum_delete(request, nid):
    """靓号删除"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/prettynum/list')
