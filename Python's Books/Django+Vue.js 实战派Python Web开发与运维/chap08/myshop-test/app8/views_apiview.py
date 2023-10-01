# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-01 8:03
"""
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.decorators import cache_response
from app8.models import Goods
from app8.serializers import GoodsSerializer


class GoodsView(APIView):
    @cache_response(timeout=60 * 1, cache='default')
    def get(self, request, *args, **kwargs):
        # 获取queryset
        goods = Goods.objects.all()[:10]
        # 开始序列化,多条数据，加上many=True
        goods_json = GoodsSerializer(goods, many=True)
        # 返回序列化对象。goods_json.data是序列化后的值
        print(goods_json.data)
        return Response(goods_json.data)

    def post(self, request):
        data = request.data  # 接收前端请求的各种数据
        print("1223" + str(request.data))
        ser_data = GoodsSerializer(data=data, many=False)
        if ser_data.is_valid():  # 判断数据的合法性
            goods = ser_data.save()  # 保存数据，实际上调用create方法
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)

    def put(self, request, *args, **kwargs):
        data = request.data  # 接收前端请求的各种数据
        try:
            goods = Goods.objects.get(id=kwargs.get("id"))
        except Goods.DoesNotExist:
            raise Http404
        ser_data = GoodsSerializer(goods, data=request.data, context={'request': request})
        if ser_data.is_valid():  # 判断数据的合法性
            goods = ser_data.save()  # 保存数据，实际上调用update方法
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        goods = Goods.objects.filter(id=kwargs.get("id"))
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
