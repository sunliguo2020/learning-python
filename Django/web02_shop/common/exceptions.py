# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-13 19:45
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def except_handler(exc, context):
    response = exception_handler(exc, context)
    if not response:
        # 如果response为None，则为DRF未处理的系统视图内部错误，可以在此处自定义处理方法：
        data = {
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'errors': '服务器内部错误',
        }
        response = Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
    # 如果是DRF已经处理过的异常，在此统一修改返回数据的字段！
    data = {
        'status_code': response.status_code,
        'errors': response.data.get('detail') or response.data,
    }
    response.data = data
    return response
