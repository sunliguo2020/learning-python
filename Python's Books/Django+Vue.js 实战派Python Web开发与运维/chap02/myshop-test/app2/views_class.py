# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 11:26
"""
from django.views.generic import TemplateView, ListView,DetailView
from . import models


class TestTemplateViews(TemplateView):
    # 设置模板文件
    template_name = '2/test_templateview.html'

    # 重写父类的get_context_data()方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context['info'] = '该变量可以传递到模板'
        return context


class TestListView(ListView):
    '''
    列表视图类
    '''
    model = models.UserBaseInfo
    template_name = '2/test_listview.html'

    # 设置模板变量的上下文
    context_object_name = "users"

    # 每页显示的条数
    paginate_by = 1
    queryset = models.UserBaseInfo.objects.filter(status=1)

    # 重写父类的get_queryset()方法
    def get_queryset(self):
        # 返回状态为1的数据
        userinfo = models.UserBaseInfo.objects.filter(status=1)
        return userinfo

    # 重写父类的get_context_data()方法
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context['info'] = 'Listview变量可以传递到模板'
        print(context)
        """
        {'paginator': <django.core.paginator.Paginator object at 0x0000026FDB47A4D0>,
         'page_obj': <Page 1 of 1>,
          'is_paginated': False,
           'object_list': <QuerySet [<UserBaseInfo: 1>]>,
            'users': <QuerySet [<UserBaseInfo: 1>]>, 
            'view': <app2.views_class.TestListView object at 0x0000026FDB430E50>,
             'info': 'Listview变量可以传递到模板'
             }
        """
        return context


class TestDetailView(DetailView):
    model = models.UserBaseInfo
    template_name = '2/test_detaiview.html'
    context_object_name = 'users'

    #对应路由中的参数userid
    pk_url_kwarg = 'userid'

