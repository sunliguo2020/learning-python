# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-01 7:55
"""
from django.urls import path

from . import views_api_view, views_apiview, views, views_mixin, views_generics

urlpatterns = [
    # path('goods/', views.GoodsListView.as_view()),
    path('goods/', views.GoodsView.as_view()),

    path('goods_jsonResponse/', views.GoodsListViewJsonResponse.as_view()),

    path('goods1/', views_api_view.GoodsList),
    path('goods1/<pk>/', views_api_view.GoodsList),
    path('goods2/', views_apiview.GoodsView.as_view()),
    path('goods2/<id>/', views_apiview.GoodsView.as_view()),

    path('goods3/', views_mixin.GoodsView.as_view()),
    path('goods3/<pk>/', views_mixin.GoodsDetailView.as_view()),

    path('goods4/', views_generics.GoodsView.as_view()),
    path('goods4/<pk>/', views_generics.GoodsDetailView.as_view()),

]
