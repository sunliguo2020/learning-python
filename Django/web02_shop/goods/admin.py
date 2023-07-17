from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.GoodsGroup)
class GoodsGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


@admin.register(models.Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'group',
                    'price',
                    'stock',
                    'sales',
                    'is_on'
                    ]


@admin.register(models.Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['goods',
                    'producer',
                    'norms',
                    ]


@admin.register(models.GoodsBanner)
class GoodsBannerAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'status',
                    'seq',
                    ]