from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.basic.models import Address
from apps.basic.serializers import AddressModelSerializer
from common.custommodelviewset import CustomModelViewSet
from common.permissions import IsOwnerOrReadOnly


class AddressViewset(CacheResponseMixin,CustomModelViewSet):
    '''
    用户地址视图类
    list：
        获取用户地址
    create：
        新增用户地址
    update：
        修改用户地址
    delete：
        删除用户地址
    '''
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressModelSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_default',)

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    #def get_object(self):
        #return self.request.user

