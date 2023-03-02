# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/15 15:57
"""
from django.shortcuts import render, redirect, HttpResponse


def chart_list(request):
    """
    数据统计页面
    """
    return render(request, 'chart_list.html')


def chart_edit(request):
    return None
