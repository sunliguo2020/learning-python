# -*- coding: utf-8 -*-

import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView


def phone_validator(value):
    print(value)
    if not re.match(r"^(1[3|4|5|6|7|8|9])\d{9}$", value):
        raise ValidationError('手机格式错误')


class MessageSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号', validators=[phone_validator, ])


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({"status": True})


class MessageView(APIView):
    def get(self, request, *args, **kwargs):
        # 1、获取手机号
        # <class 'django.http.request.QueryDict'>
        print(type(request.query_params))
        # <QueryDict: {'phone': ['15689266171']}>
        print(request.query_params)

        # 2、校验手机号
        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({'error': False, "message": "手机格式错误!"})
        phone = ser.validated_data.get('phone')

        # 3、生成随机验证码
        import random
        random_code = random.randint(1000, 9999)

        return Response({'status': True, "data": {"phone": ser.validated_data.get('phone'),
                                                  "code": str(random_code)
                                                  }
                         })
        # 4、验证码发送到手机
        # 5、验证码+手机号保留（30s过期）

        return Response({'status': True,"message":"发送成功！"})
