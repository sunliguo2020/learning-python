from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.users import forms
from apps.users.models import MyUser
from .forms import UsersForm


# Create your views here.
def add(request):
    return render(request, 'shop/users/add.html')


def edit(request, id):
    # print(id)
    # user = MyUser.objects.filter(id=id).first()
    user = MyUser.objects.get(id=id)
    # print(user)
    if request.method == 'GET':
        user_form = UsersForm(instance=user)
        context = {
            'user_form': user_form
        }
        return render(request, 'shop/users/edit.html', context)
    elif request.method == "POST":
        user_form = UsersForm(data=request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('users:users_index'))
        else:
            context = {
                'user_form': user_form
            }
            return render(request, 'shop/users/edit.html',context)


def index(request):
    if request.method == "GET":
        level = request.GET.get('level')
        truename = request.GET.get('truename', '')
        status = request.GET.get('status')
        search_dict = dict()
        if level:
            search_dict['level'] = level
        if truename:
            search_dict['truename'] = truename
        if status:
            search_dict['status'] = status

        datas = MyUser.objects.filter(**search_dict).order_by('-id')
        page_size = 2  # 每页显示的行数
        try:
            if not request.GET.get("page"):
                curr_page = 1
            curr_page = int(request.GET.get("page"))
        except:
            curr_page = 1

        paginator = Paginator(datas, page_size)
        try:
            users = paginator.page(curr_page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(1)

        context = {
            'level': level,
            'truename': truename,
            'status': status,
            'users': users,
        }

    return render(request, 'shop/users/index.html', context=context)


def delete(request, id):
    obj = MyUser.objects.get(id=id)
    obj.delete()
    json_dict = {}
    json_dict['code'] = 200
    json_dict['msg'] = '删除数据成功'
    return JsonResponse(json_dict)


def user_reg(request):
    """
    用户注册视图
    """
    if request.method == 'GET':
        form_obj = forms.UserRegForm()
        return render(request, 'shop/user_reg.html', {'form_obj': form_obj})
    if request.method == "POST":
        # form_obj = forms.UserRegForm(request.POST, request.FILES)
        form_obj = forms.UserRegForm(data=request.POST, files=request.FILES)
        if form_obj.is_valid():
            uname = request.POST.get("username", '')
            users = MyUser.objects.filter(username=uname)
            if users:
                for user in users:
                    user_img = user.user_img
                info = '用户已经存在'
            else:
                # 去掉二次输入的密码
                form_obj.cleaned_data.pop("re_password")
                form_obj.cleaned_data["is_staff"] = 1
                form_obj.cleaned_data["is_superuser"] = 0  # 非管理员
                # 接收页面传递过来的参数，进行用户新增
                user = MyUser.objects.create_user(**form_obj.cleaned_data)
                user_img = user.user_img
                info = '注册成功,请登陆'
            return render(request, 'shop/user_reg.html', {"form_obj": form_obj, "info": info, "user_img": user_img})
        else:
            errors = form_obj.errors
            # print(errors)
            return render(request, "shop/user_reg.html", {'form_obj': form_obj, 'errors': errors})


def user_login(request):
    """
    用户登录视图
    """
    return render(request, 'shop/user_login.html')


def ajax_login_data(request):
    uname = request.POST.get('username', '')
    pwd = request.POST.get('password', '')
    json_dict = {
    }
    if uname and pwd:  # 用户名和密码不为空，则查询数据库
        if MyUser.objects.filter(username=uname):  # 判断用户是否存在
            # 如果存在则验证
            user = authenticate(username=uname, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    json_dict['code'] = 1000
                    json_dict['msg'] = '登录成功'
                else:
                    json_dict['code'] = 1001
                    json_dict['msg'] = '用户还未激活'
            else:
                json_dict['code'] = 1003
                json_dict['msg'] = '用户账号有误，请查询'
        else:
            json_dict['code'] = 1004
            json_dict['msg'] = '用户名或密码为空'
        return JsonResponse(json_dict)
