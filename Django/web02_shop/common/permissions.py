# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-14 13:34
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """控制对象级别的权限"""

    def has_object_permission(self, request, view, obj):
        # 如果是管理员用户，则可以进行所有操作，否则只能用户自己的数据
        if request.user.is_superuser:
            return True
        # 校验用户
        return obj == request.user
