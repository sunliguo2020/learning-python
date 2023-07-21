# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-16 18:13
定义DRF框架的序列化器

"""
from rest_framework import serializers

from app1.models import UserInfo, Addr


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        # extra_kwargs = {
        #     'pwd': {'min_value': 0,
        #             'required': True},
        # }

    def validate_pwd(self, value):
        """自定义的字段校验器"""
        if 10 < len(value) < 18:
            raise serializers.ValidationError('pwd长度需要在10-18之间')


class AddrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addr
        fields = "__all__"
