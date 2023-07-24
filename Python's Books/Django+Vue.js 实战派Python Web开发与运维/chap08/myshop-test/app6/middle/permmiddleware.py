# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-20 14:36
"""
import re

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        #获取当前的路径
        curr_path = request.path
        print(curr_path)
        # 白名单处理
        white_list = ['/myuser_login/','myuser_reg/']
        for w in white_list:
            if re.search(w,curr_path):
                return None
        #   验证是否登录
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect('/myuser_login/')

