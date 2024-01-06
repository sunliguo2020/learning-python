# 全站 标签

from django import template

from ..models import Category, SideBar, Post

register = template.Library()


@register.simple_tag
def get_category_list():
    # 全站分类
    return Category.objects.all()


@register.simple_tag
def get_sidebar_list():
    # 侧边栏
    return SideBar.get_sidebar()


@register.simple_tag
def get_new_post():
    # 获取最新文章
    return Post.objects.order_by('-pub_date')[:8]


@register.simple_tag
def get_archives():
    # 文章归档
    return Post.objects.dates('add_date', 'month', order='DESC')[:8]
