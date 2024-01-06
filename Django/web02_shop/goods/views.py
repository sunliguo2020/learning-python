from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from goods.models import Goods, GoodsGroup, GoodsBanner, Collect
from .permissions import CollectPermission
from .serializers import GoodsSerializer, GoodsGroupSerializer, GoodsBannerSerializer, CollectSerializer


# Create your views here.


class Index(APIView):
    def get(self, request):
        """商品首页接口"""
        # 获取商品所有的分类信息
        group = GoodsGroup.objects.filter(status=True)
        group_ser = GoodsGroupSerializer(group, many=True)
        # 获取商品的海报
        banner = GoodsBanner.objects.filter(status=True)
        banner_ser = GoodsBannerSerializer(banner, many=True)
        # 获取所有的推荐商品
        goods = Goods.objects.filter(recommend=True)
        goods_ser = GoodsSerializer(goods, many=True)

        result = {
            "group": group_ser.data,
            "banner": banner_ser.data,
            "goods": goods_ser.data
        }
        return Response({"message": result})


class GoodsView(ReadOnlyModelViewSet):
    """商品视图集
    获取商品列表
    获取单个商品
    """
    queryset = Goods.objects.filter(is_on=True)
    serializer_class = GoodsSerializer

    # 实现通过商品分类和是否推荐 过滤
    filterset_fields = ("recommend", "group")

    # 通过价格和销量排序
    ordering_fields = ('sales', 'price')


class CollectViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """
    create：收藏商品
    delete：取消收藏
    list：收藏列表接口
    """
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer

    # 设置认证用户才能有权访问
    permission_classes = [IsAuthenticated, CollectPermission]

    def create(self, request, *args, **kwargs):
        """收藏商品"""
        # 获取请求参数
        user = request.user
        params_user_id = request.data.get('user')

        if user.id != params_user_id:
            return Response({"error": "您没有操作其他用户权限！"})

        # 调用继承过来的方法进行创建
        return super().create(request, *args, **kwargs)
