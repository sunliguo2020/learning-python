# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-01 7:23
"""
from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):
    """
    订单序列化器
    """

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderGoodsSerializer(serializers.ModelSerializer):
    """
    订单商品序列化器
    """

    class Meta:
        model = models.OrderGoods
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    评论序列化器
    """

    class Meta:
        model = models.Comment
        fields = "__all__"
