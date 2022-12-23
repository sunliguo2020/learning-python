from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    # admin.site.
    list_display = ['name', 'logo', 'sort', 'create_time']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'sort', 'images']


@admin.register(Goods)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name']
