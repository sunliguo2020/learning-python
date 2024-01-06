from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import models
from . import serializers
from .permissions import CartPermission
from .serializers import ReadCartSerializer


# Create your views here.
class CartView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               GenericViewSet):
    """
    购物车模块
    """

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    permission_classes = [IsAuthenticated, CartPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReadCartSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        # 获取用户信息
        user = request.user

        # 获取参数
        goods = request.data.get('goods')

        # 校验参数
        # 1、校验改用户的购物车中是否有改商品
        if models.Cart.objects.filter(user=user, goods=goods).exists():
            # 用户已经添加过改商品到购物车，直接修改商品的数量
            # cart_goods = models.Cart.objects.get(user=user, goods=goods)
            cart_goods = models.Cart.objects.filter(user=user, goods=goods).first()
            cart_goods.number += 1
            cart_goods.save()
            # 对购物车新增商品进行序列化
            serializers = self.get_serializer(instance=cart_goods)

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            # 没有商品，则调用继承的create方法进行创建
            request.data['user'] = user.id
            # 方式1：
            # serializer = self.get_serializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # self.perform_create(serializer)
            # headers = self.get_success_headers(serializer.data)
            #
            # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

            # 方式2：
            return super().create(request, *args, **kwargs)
        # 添加商品到购物车

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset().filter(user=request.user)
        serializers = self.get_serializer(queryset, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def update_goods_status(self, request, *args, **kwargs):
        # 修改商品的选中状态

        instance = self.get_object()
        # 判断当前obj 的user是否是当前登录用户
        if not instance.user == request.user:
            return Response({"error": "不能修改非当前用户的购物车!"})
        #  修改自己的购物车商品状态
        instance.is_checked = not instance.is_checked
        instance.save()
        return Response({'message': "修改成功"}, status=status.HTTP_200_OK)

    def update_goods_number(self, request, *args, **kwargs):
        """修改购物车商品数量"""
        # 获取参数
        number = request.data.get('number')
        instance = self.get_object()

        if not isinstance(number, int):
            return Response({"error": "参数number只能是int类型，并且不能为空！"},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改商品的数量
        if number <= 0:
            # 删除该商品
            instance.delete()
            return Response({"message": "已经从购物车中移除"},
                            status=status.HTTP_200_OK)
        elif number > instance.goods.stock:
            return Response({"message": "数据不能高过该商品的库存！"},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            instance.number = number
            instance.save()
            return Response({"message": "修改成功"},
                            status=status.HTTP_200_OK)
