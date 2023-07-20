# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-16 18:13
定义DRF框架的序列化器

"""
from rest_framework import serializers

from app1.models import UserInfo


class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=18)
    pwd = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=40)
    age = serializers.IntegerField(min_value=0, max_value=150)

    def create(self, validated_data):
        """
        自定义一个序列化器保存数据的方法
        :param validated_data:
        :return:
        """
        UserInfo.objects.create(validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.pwd = validated_data['pwd']
        instance.email = validated_data['email']
        instance.age = validated_data['age']

        instance.save()
        return instance


class AddrSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    mobile = serializers.CharField(max_length=18)
    city = serializers.CharField(max_length=20)
    info = serializers.CharField(max_length=200)

    # 关联字段序列化
    user = serializers.PrimaryKeyRelatedField(read_only=True)
