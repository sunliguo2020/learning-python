# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-14 13:16
"""
from rest_framework import serializers

from users.models import User, Addr


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""

    class Meta:
        model = User
        # fields = "__all__"
        fields = ['id', 'username', 'email', 'mobile', 'avatar', 'last_name']


class AddressSerializer(serializers.ModelSerializer):
    """收货地址模型序列化器"""

    class Meta:
        model = Addr
        fields = "__all__"
