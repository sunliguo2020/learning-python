from django.shortcuts import render
from django.views import View

from apps.goods.forms import *
from apps.goods.myfilter import GoodsFilter
from apps.goods.serializers import *
from apps.goods.mypage import *
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.response import Response

from common.custommixins import CustomListModelMixin, CustomRetrieveModelMixin
from common.custommodelviewset import CustomModelViewSet


class GoodsCategoryViewset(CacheResponseMixin,CustomListModelMixin,CustomRetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(parent__isnull=True)
    serializer_class = GoodsCategoryModelSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class IndexCategoryGoodsViewSet(CustomListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(parent__isnull=True)
    serializer_class = IndexCategoryGoodsSerializer

class GoodsCategoryView(View):
    def get(self,request):
        cates=GoodsCategory.objects.all()
        return render(request,"shop/goods/cate_index.html",{"cates":cates})

    def post(self,request):
        pass

class SlideViewset(CustomModelViewSet):
    '''
    首页轮播图的商品
    '''
    queryset = Slide.objects.all().order_by("sort")
    serializer_class = SlideModelSerializer
    #pagination_class = MyPage

class GoodsView_Custom(CacheResponseMixin,CustomModelViewSet):
    """
    list:
        返回所有数据.
    retrieve:
        返回单条数据实例.
    create:
        新增数据
    update:
        修改数据
    partial_update:
        修改部分数据
    delete:
        删除数据
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class=MyPage
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name', 'price')
    filterset_class=GoodsFilter
    #permission_classes=(permissions.IsAuthenticated,IsOwnerOrReadOnly)
    #搜索
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields=('name','price')
    #排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    ordering_fields=('id','name','price')


class GoodsView(CacheResponseMixin,CustomModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerializer
    pagination_class=MyPage
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filterset_class=GoodsFilter
    #搜索
    search_fields=('name','goods_desc')
    ordering_fields=('amount','price')

    def retrieve(self,request,*args, **kwargs):
        instance=self.get_object()
        instance.click_num+=1
        instance.save()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)