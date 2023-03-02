# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 9:33
"""
from django.urls import path, re_path
from . import views
from .views_class import TestTemplateViews,TestListView,TestDetailView

urlpatterns = [
    path('app2/index/', views.index),
    path('show/<int:id>/', views.show),  # <>中的内容为URL参数,语法格式为：<参数数据类型:参数名称>
    path('app2/article/<uuid:id>/', views.show_uuid, name="show_uuid"),
    path('app2/article/<slug:q>/', views.show_slug, name="show_slug"),
    re_path('app2/list/(?P<year>\d{4})/', views.article_list, name="article_list"),
    path('app2/url_reverse/', views.url_reverse, name="app2_url_reverse"),
    path('app2/hello/', views.hello, name="app2_hello"),
    path('app2/test_get/', views.test_get, name="app2_test_get"),
    path('app2/test_render/', views.test_render, name='app2_test_render'),

    # 测试redirect() 函数实现页面重定向
    path('app2/test_redirect_model/<int:id>/', views.test_redirect_model, name='app2_test_redirect_model'),
    path('app2/userinfo/<int:id>/', views.userinfo, name='app2_userinfo'),

    # 视图类
    # 视图类在调用的时，只能是函数的方式，而不能是类的方式。将视图类as_views()转化为视图函数
    path('indexpage/', views.IndexPageView.as_view()),
    # 通用视图类 TemplateView
    path('app2/test_templateview/', TestTemplateViews.as_view()),
    # 列表视图类 ListView
    path('app2/test_listview/', TestListView.as_view()),
    # 详细视图类 DetailView
    path('app2/test_detailview/<int:userid>/', TestDetailView.as_view()),
]
