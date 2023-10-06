from django.contrib import admin

from .models import Books, Record


# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


@admin.register(Record)
class RecordAmdin(admin.ModelAdmin):
    list_display = ['id', 'book', 'name', 's_time', 'e_time', 'status']
