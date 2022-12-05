# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:03
"""
import copy

from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from app01.utils.pageination import Pagination
from app01.utils.form import ShoujihaoModelsForm


def shoujihao_list(request):
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    query_dict = request.GET

    if search_data:
        # 查询条件
        data_dict['BUSI_NBR__contains'] = search_data

    queryset = models.Shoujihao.objects.filter(**data_dict).order_by('mod_time')
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data,
        "query_dict": query_dict.urlencode()
    }

    return render(request, 'shoujihao_list.html', context)


def shoujihao_edit(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    row_obj = models.Shoujihao.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ShoujihaoModelsForm(instance=row_obj)
        return render(request, "shoujihao_edit.html", {"form": form})

    form = ShoujihaoModelsForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        new_quereyset = models.Shoujihao.objects.filter(id=nid)
        return render(request, 'shoujihao_list.html', {"queryset": new_quereyset})

    return render(request, "shoujihao_edit.html", {"form": form})


def shoujihao_delete(request, nid):
    """

    :param request:
    :param nid:
    :return:
    """
    models.Shoujihao.objects.filter(id=nid).delete()
    query_dict = copy.deepcopy(request.GET)
    query_dict._mutable = True
    # print(query_dict)
    # 删除后，跳转的页面包含上一页的查询参数
    return redirect(f'/shoujihao/list/?{query_dict.urlencode()}')
