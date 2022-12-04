# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 21:25
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """
    检查是否已经登录
    """
    def process_request(self, request):

        next_url = request.path_info
        # print(next_url)
        if not next_url.startswith('/login/'):
            # 检查用户是否已经登录，，未登录，跳转到登录页面
            # 用户发来请求，获取cookie随机字符串，拿着随机字符串
            info = request.session.get('info')
            if not info:
                return redirect('/login/')

    def process_response(self, request, response):
        return response
