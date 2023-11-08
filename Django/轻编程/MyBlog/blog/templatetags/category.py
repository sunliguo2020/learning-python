# 全站 标签

from django import template

from ..models import Category,SideBar
register = template.Library()

@register.simple_tag
def get_category_list():
    # 全站分类
    return Category.objects.all()

@register.simple_tag
def get_sidebar_list():
    # 侧边栏
    return SideBar.get_sidebar()