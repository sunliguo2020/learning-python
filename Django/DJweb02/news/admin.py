from django.contrib import admin

from .models import NewsInfo


# Register your models here.

@admin.register(NewsInfo)
class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
