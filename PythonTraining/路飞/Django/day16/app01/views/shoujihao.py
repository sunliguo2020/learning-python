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

    # 是否显示某条数据
    data_dict['is_active'] = True

    queryset = models.Shoujihao.objects.filter(**data_dict)[:]
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
    删除手机号的某行记录
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


def shoujihao_active(request, nid):
    """
    隐藏某行数据
    :param request:
    :param nid:
    :return:
    """
    models.Shoujihao.objects.filter(id=nid).update(is_active=False)
    query_dict = copy.deepcopy(request.GET)
    query_dict._mutable = True
    # print(query_dict)
    # 删除后，跳转的页面包含上一页的查询参数
    return redirect(f'/shoujihao/list/?{query_dict.urlencode()}')


def shoujihao_test(request):
    """
    手机号数据库测试
    :param request:
    :return:
    """
    # 查询所有没有隐藏的数据
    queryset = models.Shoujihao.objects.filter(is_active=True)
    print(type(queryset))  # print(type(queryset))

    print(queryset.values)
    # <bound method QuerySet.values of <QuerySet [<Shoujihao: Shoujihao object (1)>, <Shoujihao: Shoujihao object (2)>, <Shoujihao: Shoujihao object (3)>, <Shoujihao: Shoujihao object (4)>, <Shoujihao: Shoujihao object (5)>, <Shoujihao: Shoujihao object (6)>, <Shoujihao: Shoujihao object (7)>, <Shoujihao: Shoujihao object (8)>, <Shoujihao: Shoujihao object (9)>, <Shoujihao: Shoujihao object (10)>, <Shoujihao: Shoujihao object (11)>, <Shoujihao: Shoujihao object (12)>, <Shoujihao: Shoujihao object (13)>, <Shoujihao: Shoujihao object (14)>, <Shoujihao: Shoujihao object (15)>, <Shoujihao: Shoujihao object (16)>, <Shoujihao: Shoujihao object (17)>, <Shoujihao: Shoujihao object (18)>, <Shoujihao: Shoujihao object (19)>, <Shoujihao: Shoujihao object (20)>, '...(remaining elements truncated)...']>>

    # for value in queryset.values():
    #     print(value)
    # print(len(queryset.values('BUSI_NBR').distinct()))

    # 手机号和身份证号都不重复的数据
    for item in queryset.values('id', 'BUSI_NBR', 'CERTIFICATES_NBR').distinct()[:10]:
        print(item)  # {'id': 1, 'BUSI_NBR': '13065049970', 'CERTIFICATES_NBR': '37012419961118754X'}
        id, phone, idcard = item.values()
        # print(id,phone,idcard)
        # new_quereyset = models.Shoujihao.objects.exclude(id=id, is_active=False).filter(BUSI_NBR__contains=phone,
        #                                                                                 CERTIFICATES_NBR__contains=idcard).update(
        #     is_active=False)
        # # print(new_quereyset)
    context = {
        # "queryset": queryset
    }
    return render(request, 'shoujihao_list.html', context)
