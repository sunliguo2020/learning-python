from typing import get_origin
from django.shortcuts import render,get_object_or_404

from .models import Category, Post


# Create your views here.
def index(request):
    # 首页
    category_list = Category.objects.all()  # 查询到所有的分类
    post_list = Post.objects.all()  # 查询到所有的文章
    context = {"category_list": category_list, "post_list": post_list}  # 上下文数据

    return render(request, "blog/index.html", context)

def category_list(request,category_id):
    category= get_object_or_404(Category,id=category_id)
    # 获取当前分类下的所有文章
    posts = category.post_set.all()
    context = {
        'category':category,
        'post_list':posts
    }
    return render(request,'blog/list.html',context)

def post_detail(request,post_id):
    # 文章详情页
    post = get_object_or_404(Post,id=post_id)
    context = {
        'post':post
    }

    return render(request,'blog/detail.html',context)