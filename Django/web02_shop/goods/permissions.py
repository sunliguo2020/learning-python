# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-27 19:08
"""
from rest_framework import permissions


class CollectPermission(permissions.BasePermission):
    """商品收藏对象操作权限"""

    def has_object_permission(self, request, view, obj):
        # 判断登录的账号是否是管理员
        if request.user.is_superuser:
            return True
        # 如果不是管理员，则判断操作的用户对象和登录的用户是否是同一个用户
        return obj.user == request.user
