from rest_framework import serializers
from .models import *
from django.db.models import Q


class GoodsSerializer(serializers.Serializer):
    name=serializers.CharField(required=True,max_length=100)
    click_num=serializers.IntegerField(default=0)

class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields="__all__"

class CategorySerializerSub(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsCategoryModelSerializer(serializers.ModelSerializer):
    sub_cat=CategorySerializerSub(many=True)
    class Meta:
        model=GoodsCategory
        fields="__all__"

class SlideModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slide
        fields="__all__"

class IndexCategoryGoodsSerializer(serializers.ModelSerializer):
    '''
    首页部分分类下的商品展示
    '''
    sub_cat=CategorySerializerSub(many=True)
    goods = serializers.SerializerMethodField()

    #每个分类下需要显示商品，因此增加了一个goods字段，类型为SerializerMethodField
    #之后通过get_字段的方式取出与这个goods对象关联的一系列内容。我们这里要取出图片、名称、价格、销售价

    def get_goods(self,obj):
        goods=Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_id=obj.id))

        serializer=GoodsModelSerializer(goods, many=True,context={'request':self.context['request']})
        return serializer.data

    class Meta:
        model=GoodsCategory
        fields="__all__"