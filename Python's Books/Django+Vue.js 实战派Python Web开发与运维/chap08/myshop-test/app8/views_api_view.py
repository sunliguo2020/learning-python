# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-01 7:41
"""
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app8.models import Goods
from app8.serializers import GoodsSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def GoodsList(request, *args, **kwargs):
    if request.method == "GET":
        # 获取queryset
        if kwargs.get("id"):
            id = kwargs.get("id")
            goods = Goods.objects.filter(id=id)
        else:
            goods = Goods.objects.all()[:10]
        # 开始序列化,多条数据，加上many=True
        goods_json = GoodsSerializer(goods, many=True)
        # 返回序列化对象。goods_json.data是序列化后的值
        print(goods_json.data)
        return Response(goods_json.data)

    elif request.method == "POST":
        data = request.data  # 接收前端请求的各种数据
        print("1223" + str(request.data))
        ser_data = GoodsSerializer(data=data, many=False)
        if ser_data.is_valid():  # 判断数据的合法性
            goods = ser_data.save()  # 保存数据，实际上调用create方法
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        data = request.data  # 接收前端请求的各种数据
        try:
            goods = Goods.objects.get(id=kwargs.get("id"))
        except Goods.DoesNotExist:
            raise Http404
        ser_data = GoodsSerializer(goods, data=request.data, context={'request': request})
        if ser_data.is_valid():  # 判断数据的合法性
            goods = ser_data.save()  # 保存数据，实际上调用create方法
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        goods = Goods.objects.filter(id=kwargs.get("id"))
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
