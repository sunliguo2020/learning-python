# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-28 19:36
"""
from rest_framework import serializers

from goods.serializers import GoodsSerializer
from . import models


class CartSerializer(serializers.ModelSerializer):
    """购物车序列化器"""

    class Meta:
        model = models.Cart
        fields = "__all__"


class CartInfoSerializer(serializers.ModelSerializer):
    # 返回商品名称
    goods = GoodsSerializer()

    class Meta:
        model = models.Cart
        fields = "__all__"
