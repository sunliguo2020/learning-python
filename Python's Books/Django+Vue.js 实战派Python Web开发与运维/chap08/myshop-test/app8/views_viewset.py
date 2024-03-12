# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-07 13:01
"""
# from common.permission import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets

from .models import Goods
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = MyPage
    permission_classes = (permissions.IsAuthenticated,
                          # IsOwnerOrReadOnly
                          )
