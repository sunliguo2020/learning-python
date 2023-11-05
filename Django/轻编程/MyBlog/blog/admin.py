from django.contrib import admin

# Register your models here.

from .models import Category, Post, Tag

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)