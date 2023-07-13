import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User


class LoginView(TokenObtainPairView):
    """
    用户登录
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # 自定义登录成功后返回的结果
        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['mobile'] = serializer.user.mobile
        result['email'] = serializer.user.email
        result['username'] = serializer.user.username

        result['token'] = result.pop('access')

        return Response(result, status=status.HTTP_200_OK)


class RegisterView(ViewSet):
    def create(self, request):
        pass


class RegisterView2(APIView):
    """注册视图"""

    def post(self, request):
        """注册接口"""
        # 一、接收用户参数
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        # 二、参数校验
        # 1 校验参数是否为空
        if not all([username, email, password, password_confirmation]):
            return Response({'error': "所有参数不能为空！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 2 用户名是否已注册
        if User.objects.filter(username=username).exists():
            return Response({'error': "用户名已经存在！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 3 校验两次密码是否一致
        if password != password_confirmation:
            return Response({'error': "两次密码不一致！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 4 校验密码长度
        if not (6 <= len(password) <= 18):
            return Response({'error': "密码长度需要6到18位之间！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 5 校验邮箱是否存在
        if User.objects.filter(email=email).exists():
            return Response({'error': "该邮箱已被其他用户使用！"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 6、校验邮箱格式是否正确
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return Response({'error': "邮箱格式不正确！"}, status=status.HTTP_400_BAD_REQUEST)

        # 三、创建用户
        obj = User.objects.create_user(username=username, email=email, password=password)
        res = {
            'username': username,
            'id': obj.id,
            'email': obj.email,
        }
        return Response(res, status=status.HTTP_201_CREATED)
