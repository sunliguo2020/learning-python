# 全站 标签

from django import template

from ..models import Category
register = template.Library()

@register.simple_tag
def get_category_list():
    return Category.objects.all()