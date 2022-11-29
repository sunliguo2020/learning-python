from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")
def user_list(request):
    return HttpResponse("用户列表")