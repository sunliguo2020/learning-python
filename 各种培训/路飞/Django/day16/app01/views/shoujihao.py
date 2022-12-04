# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:03
"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pageination import Pagination
from app01.utils.form import ShoujihaoModelsForm


def shoujihao_list(request):
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")

    if search_data:
        # 查询条件
        data_dict['BUSI_NBR__contains'] = search_data

    queryset = models.Shoujihao.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data,
    }

    return render(request, 'shoujihao_list.html', context)


def shoujihao_edit(request, nid):
    if request.method == "GET":
        row_obj = models.Shoujihao.objects.filter(id=nid).first()
        form = ShoujihaoModelsForm(instance=row_obj)
        return render(request, "shoujihao_edit.html", {"form": form})

    return None


def shoujihao_delete(request, nid):
    models.Shoujihao.objects.filter(id=nid).delete()
    return redirect('/shoujihao/list')
