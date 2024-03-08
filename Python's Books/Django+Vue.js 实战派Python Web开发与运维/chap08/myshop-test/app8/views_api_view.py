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

from .models import Goods
from .serializers import GoodsSerializer


# 允许以GET POST PUT DELETE 方式请求视图函数
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def GoodsList(request, *args, **kwargs):
    if request.method == "GET":
        # 获取queryset
        print("GoodsList中 args，kwarg", args, kwargs)
        # 判断是否传入了pk
        if kwargs.get("pk"):
            pk = kwargs.get("pk")
            goods = Goods.objects.filter(id=pk)
        else:
            goods = Goods.objects.all()[:10]
        # 开始序列化,多条数据，加上many=True
        goods_json = GoodsSerializer(instance=goods, many=True)
        # 返回序列化对象。goods_json.data是序列化后的值
        print(goods_json)
        return Response(goods_json.data)

    elif request.method == "POST":
        data = request.data  # 接收前端请求的各种数据
        print("接收到前端的数据:", request.data)
        ser_data = GoodsSerializer(data=data, many=False)
        if ser_data.is_valid():  # 判断数据的合法性
            # 序列化器的save方法，判断
            goods = ser_data.save()  # 保存数据，实际上调用create方法
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        print('GoodsList中 PUT 请求')
        data = request.data  # 接收前端请求的各种数据
        try:
            goods = Goods.objects.get(id=kwargs.get("pk"))
        except Goods.DoesNotExist:
            raise Http404
        ser_data = GoodsSerializer(instance=goods, data=request.data, context={'request': request})
        if ser_data.is_valid():  # 判断数据的合法性
            goods = ser_data.save()  # 保存数据，实际上调用create方法
            return Response(ser_data.data, status=status.HTTP_200_OK)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        goods = Goods.objects.filter(id=kwargs.get("pk"))
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
