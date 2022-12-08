# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/8 17:40
"""
import os

from django.shortcuts import render
from app01 import models
from app01.utils.pageination import Pagination


def webcam_list(request):
    """
    显示图片列表
    :param request:
    :return:
    """
    queryset = models.Webcam.objects.all()

    page_object = Pagination(request,queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'webcam_list.html', context)
