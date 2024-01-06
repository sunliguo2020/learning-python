import os.path
import re

from django.http import FileResponse
from rest_framework import status, mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from common.permissions import UserPermission, AddrPermission
from users.models import User, Addr
from web02_shop.settings import MEDIA_ROOT
from .serializers import UserSerializer, AddressSerializer


# Create your views here.


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


class UserView(GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin):
    """用户相关操作的视图集"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 设置认证用户才能有权访问
    # permission_classes = [IsAuthenticated, UserPermission]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPermission]

    def upload_avatar(self, request, *args, **kwargs):
        """上传用户头像"""
        avatar = request.data.get('avatar')
        # 校验是否有上传文件
        if not avatar:
            return Response({"error": '上传失败，文件不能为空！'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 校验文件大小不能超过300kb
        if avatar.size > 1024 * 300:
            return Response({"error": '上传失败，文件不能超过300Kb'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 保存文件
        user = self.get_object()
        # 获取序列化对象
        ser = self.get_serializer(user, data={'avatar': avatar}, partial=True)
        # 校验
        ser.is_valid(raise_exception=True)
        # 保存
        ser.save()

        return Response({"url": ser.data.get('avatar')})

    def update_name(self, request, *args, **kwargs):
        """修改用户昵称"""
        # 1、获取参数
        last_name = request.data.get('last_name')
        # 2、校验参数
        if not last_name:
            return Response({"error": "用户昵称必传字段,参数last_name甭能为空"},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 3、修改昵称
        user = self.get_object()
        user.last_name = last_name
        user.save()
        return Response({"message": '修改用户昵称成功!'})


class FileView(APIView):
    """
    访问上传文件的视图
    """

    def get(self, request, name):
        # 获取图片并返回
        # 通过文件名拼接完整的文件路径，并返回图片给前端
        path = MEDIA_ROOT / name
        print(path)
        if os.path.isfile(path):
            return FileResponse(open(path, 'rb'))

        return Response({'error': '文件不存在！'}, status=status.HTTP_404_NOT_FOUND)


class AddrView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin):
    """地址管理视图"""
    # 查询集（默认使用按更新时间排序）
    # queryset = Addr.objects.all().order_by('update_time')
    queryset = Addr.objects.all()
    # 序列化器
    serializer_class = AddressSerializer
    # 设置认证用户才能有权限访问
    permission_classes = [IsAuthenticated, AddrPermission]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # 通过请求过来的认证用户进行过滤
        queryset = queryset.filter(user=request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def set_default_addr(self, request, *args, **kwargs):
        """设置默认的收货地址"""
        # 1、获取到要设置的对象
        obj = self.get_object()
        obj.is_default = True
        obj.save()
        # 2、将该地址设置默认收货地址，将用户其他的收货地址设置为非默认
        # 获取用户收货地址
        queryset = self.get_queryset().filter(user=request.user)
        for item in queryset:
            if item != obj:
                item.is_default = False
                item.save()

        return Response({'message': "设置成功"}, status=status.HTTP_200_OK)
