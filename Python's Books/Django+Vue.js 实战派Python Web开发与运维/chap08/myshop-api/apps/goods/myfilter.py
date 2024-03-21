from django.db.models import Q
from django_filters import rest_framework as filters
from .models import *

class GoodsFilter(filters.FilterSet):
    #根据名称进行模糊匹配
    name=filters.CharFilter(field_name='name',lookup_expr='icontains')
    #价格区间
    max_price=filters.NumberFilter(field_name='price',lookup_expr='lte')
    min_price=filters.NumberFilter(field_name='price',lookup_expr='gte')
    category=filters.NumberFilter(method='category_filter')

    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_id=value))


    class Meta:
        model=Goods
        fields=('name','min_price','max_price')