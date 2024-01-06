from django.contrib import admin

from .models import MyUser


# Register your models here.

@admin.register(MyUser)
class MyUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'truename', 'mobile']
