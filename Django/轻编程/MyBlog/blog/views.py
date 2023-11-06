from django.shortcuts import render

from .models import Category, Post


# Create your views here.
def index(request):
    category_list = Category.objects.all()  # 查询到所有的分类
    post_list = Post.objects.all()  # 查询到所有的文章
    context = {"category_list": category_list, "post_list": post_list}  # 上下文数据

    return render(request, "blog/index.html", context)
