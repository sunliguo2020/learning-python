from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Category, Post


# Create your views here.
def index(request):
    # 首页
    category_list = Category.objects.all()  # 查询到所有的分类
    post_list = Post.objects.all()  # 查询到所有的文章
    context = {"category_list": category_list, "post_list": post_list}  # 上下文数据

    return render(request, "blog/index.html", context)


def category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # 获取当前分类下的所有文章
    posts = category.post_set.all()
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    # 文章详情页
    post = get_object_or_404(Post, id=post_id)

    # 上一篇
    prev_post = Post.objects.filter(id__lt=post_id).last()
    # 下一篇
    next_post = Post.objects.filter(id__gt=post_id).first()
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post
    }

    return render(request, 'blog/detail.html', context)


def search(request):
    """ 搜索视图 """
    keyword = request.GET.get('keyword', '')  # 获取表单中输入的值

    # 没有搜索默认显示所有文章
    if not keyword:
        post_list = Post.objects.all()
    else:
        # 包含查询的方法，用Q对象来组合复杂查询，title__icontains 他两个之间用的是双下划线（__）链接
        post_list = Post.objects.filter(
            Q(title__icontains=keyword) | Q(desc__icontains=keyword) | Q(content__icontains=keyword))

    context = {
        'post_list': post_list,
        'keyword': keyword
    }
    print(context)
    return render(request, 'blog/index.html', context)


def archives(request, year, month):
    # 文章归档列表页
    post_list = Post.objects.filter(add_date__year=year, add_date__month=month)
    context = {'post_list': post_list, 'year': year, 'month': month}
    return render(request, 'blog/archives_list.html', context)
