from django.contrib import admin
from .models import Category,Movie
# Register your models here.
admin.site.register(Category)
# admin.site.register(Movie)

@admin.register(Movie)
class MovieAdminModel(admin.ModelAdmin):
    list_display = ['moive_name']