from django.contrib import admin

from apps.users.models import *


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'truename', 'mobile']
