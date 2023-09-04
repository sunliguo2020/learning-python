from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Order)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'addr', 'order_code',
                    'amount', 'status',
                    'pay_time']


@admin.register(models.OrderGoods)
class OrderGoodsAdminModel(admin.ModelAdmin):
    list_display = ['order', 'goods', 'price', 'number']


@admin.register(models.Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ['user', 'order', 'goods', 'content', 'rate', 'star']
