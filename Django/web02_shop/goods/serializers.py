# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-23 12:28
"""
from rest_framework import serializers

from .models import Goods, GoodsGroup, GoodsBanner, Collect, Detail


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品序列化器
    """

    class Meta:
        model = Goods
        fields = "__all__"


class GoodsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsGroup
        fields = "__all__"


class GoodsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBanner
        fields = "__all__"


class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"
