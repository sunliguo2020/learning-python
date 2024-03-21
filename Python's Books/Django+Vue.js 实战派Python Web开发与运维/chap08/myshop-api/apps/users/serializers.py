import re

from django.http import JsonResponse
from rest_framework import serializers
from .models import *

#用户详情页序列化类
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=("username","truename","user_img","sex","email","mobile","level","status")

#用户修改页序列化类
class MyUserUpdateSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username=serializers.CharField(read_only=True,error_messages={
        "required":"请输入用户名",
        "blank":"用户名不允许为空",
        "min_length":"用户名长度至少为6位"
    })
    mobile=serializers.CharField(read_only=True)
    class Meta:
        model=MyUser
        fields=("username","truename","user_img","sex","email","mobile","level","status")


#用户注册序列化类
class MyUserRegSerializer(serializers.ModelSerializer):
    username=serializers.CharField(required=True,error_messages={
        "required":"请输入用户名",
        "blank":"用户名不允许为空",
        "min_length":"用户名长度至少为6位"
    })
    mobile=serializers.CharField(required=True,max_length=11)
    password=serializers.CharField(required=True,min_length=6)

    class Meta:
        model=MyUser
        fields=("username","password","mobile")

    def create(self, validated_data):
         user = super().create(validated_data=validated_data)
         user.set_password(validated_data["password"])
         user.save()
         return user

    def validate_username(self,username):
        #判断用户名是否注册
        if MyUser.objects.filter(username=username).count():
            raise serializers.ValidationError("用户名已经存在，请查询")
            #return JsonResponse({'errors': serializers.errors}, status=500)
        return username

    def validate_mobile(self,mobile):
        #判断手机号码是否注册
        if MyUser.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("手机号码已经存在，请查询")
        # 手机号码正则表达式
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        return mobile
