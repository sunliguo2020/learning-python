from django.contrib import admin
from apps.goods.models import *
@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
#设置列表中显示的字段
    list_display=['name','logo']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
#设置列表中显示的字段
    list_display=['name','market_price','price']