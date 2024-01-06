from django.contrib import admin

from .models import UserProfile, UserInfo


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth', 'phone']
    list_filter = ['phone', ]


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'company', 'profession', 'address', 'aboutme', 'photo']
    list_filter = ['school', 'company', 'profession']
