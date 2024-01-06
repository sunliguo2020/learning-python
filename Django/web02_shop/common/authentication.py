# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-14 12:01
自定义用户登录的认证类，实现多字段登录
"""
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import serializers
from users.models import User


class Authentication(ModelBackend):
    """自定义的登录认证类"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """支持使用手机号、邮箱、用户名登录"""

        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username) | Q(email=username))
        except :
            raise serializers.ValidationError({'error':'未找到该用户'})
        else:
            # 验证密码是否正确
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError({'error': '密码不正确!'})

