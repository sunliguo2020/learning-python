# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-10-29 11:05
"""
from rest_framework import generics

from .models import Goods
from .serializers import GoodsModelSerializer


class GoodsView(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerializer


class GoodsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerializer
