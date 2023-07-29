from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import models
from . import serializers


# Create your views here.
class CartView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin, GenericViewSet):
    """

    """

    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    permission_classes = [IsAuthenticated]

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
            # 对改商品进行序列化
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
