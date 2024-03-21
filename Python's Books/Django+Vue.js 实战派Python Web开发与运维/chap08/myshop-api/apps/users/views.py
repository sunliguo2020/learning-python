import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
#from notebook.auth.security import set_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.users.models import MyUser
from apps.users.serializers import *
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import authentication
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from common.custommodelviewset import CustomModelViewSet
from common.permissions import IsOwnerOrReadOnly


class MyUserViewSet(CacheResponseMixin,CustomModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserRegSerializer

    #lookup_field = "pk"
    #lookup_url_kwarg = None
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if  self.action=="create":
            return MyUserRegSerializer
        elif self.action=="retrieve":
            return MyUserUpdateSerializer
        elif self.action=="update":
            return MyUserUpdateSerializer
        
        return MyUserUpdateSerializer

    def get_permissions(self):
        if  self.action=="retrieve":
            print("retrieve")
            return [permissions.IsAuthenticated()]
        elif self.action=="update":
            return [permissions.IsAuthenticated()]
            print("update")
        else:
        #return []
            return []
    #获取当前用户
    def get_object(self):
        return self.request.user



class MyUserDetailViewSet(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserUpdateSerializer

    #authentication_classes = (permissions.IsAuthenticated,authentication.TokenAuthentication)

myuser=get_user_model()

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            myuser = MyUser.objects.get(Q(username=username)|Q(mobile=username))
            if myuser.check_password(password):
                return myuser
        except Exception as e:
            return None


def myuser_reg(request):
    if request.method=="GET":
        return HttpResponse("GET")
    elif request.method=="POST":
        uname=request.POST.get("username",'')
        pwd=request.POST.get("password",'')
        print(uname)
        print(pwd)
            #跳转到登陆页面
        return JsonResponse('{"username":["用户名已经存在，请查询"],"mobile":["手机号码已经存在，请查询"]}',safe=False,json_dumps_params={'ensure_ascii':False,"indent":4})