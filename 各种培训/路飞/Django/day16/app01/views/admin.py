# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:40
"""
from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pageination import Pagination


def admin_list(request):
    """管理员列表"""
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")

    if search_data:
        #查询条件
        data_dict['username__contains'] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "pagestring": page_object.html(),
        "search_data":search_data,
    }

    return render(request, "admin_list.html", context)
