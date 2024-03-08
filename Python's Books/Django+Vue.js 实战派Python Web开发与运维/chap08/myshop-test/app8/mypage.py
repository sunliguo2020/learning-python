# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-29 16:15
"""
from rest_framework.pagination import PageNumberPagination


class MyPage(PageNumberPagination):
    page_size = 1  # 每页显示的数量
    max_page_size = 5  # 最多设置的每页显示的数量
    page_size_query_param = 'size'  # 每页显示数量的参数名称
    page_query_param = 'page'  # 页码的参数名称
