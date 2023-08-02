from django.contrib import admin

from . import models


# Register your models here.

@admin.register(models.Cart)
class CartAdminModela(admin.ModelAdmin):
    list_display = ['id', 'user', 'goods', 'number', 'is_checked']
