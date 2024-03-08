# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-08 13:17
"""
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data.clear()
        # 组装code、msg和data
        response.data['code'] = response.status_code

        if response.data['msg'] == 405:
            response.data['msg'] = '请求不允许'
        elif response.data['msg'] == 401:
            response.data['msg'] = '认证未通过'
        elif response.data['msg'] == 403:
            response.data['msg'] = '认证未通过'
        elif response.data['msg'] == 404:
            response.data['msg'] = '未找到文件'
        elif response.data['msg'] >= 500:
            response.data['msg'] = '服务器异常'
        else:
            response.data['msg'] = '其他位置错误'

        response.data['data'] = []
    return response
