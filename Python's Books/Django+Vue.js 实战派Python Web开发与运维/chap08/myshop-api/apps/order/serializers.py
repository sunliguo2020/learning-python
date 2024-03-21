from django.db import transaction
from rest_framework import serializers
from .models import *
from apps.order.models import Cart
from ..goods.serializers import GoodsModelSerializer


class CartModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model=Cart
        fields="__all__"
    #重写create方法
    #判断当新增同一个商品，直接做update操作
    def create(self, validated_data):
        user=self.context["request"].user
        goods=validated_data["goods"]
        goods_num=validated_data["goods_num"]

        objs=Cart.objects.filter(user=user, goods=goods).first()
        print(objs)
        if objs:
                objs.goods_num+=goods_num
                objs.save()
        #不满足的话，执行新增操作
        else:
            print("else")
            objs=Cart.objects.create(**validated_data)

        return objs
    #处理put、patch操作
    def update(self, instance, validated_data):
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        print(instance)
        instance.goods_num=validated_data["goods_num"]
        instance.save()
        return  instance


class CartDetailModelSerializer(serializers.ModelSerializer):
    goods=GoodsModelSerializer(many=False)

    class Meta:
        model=Cart
        fields=("goods","goods_num")


class OrderModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Order
        fields="__all__"
