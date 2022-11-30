from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return HttpResponse("用户列表")


def user_add(request):
    return HttpResponse("添加用户")


def tpl(request):
    # 去app目录下的templates目录寻找tpl.html,(根据app的注册顺序，逐一去他们的templates目录中寻找
    name = '韩超'
    return render(request, 'tpl.html', {"a1": name})
