from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render

from apps.users import forms
from apps.users.models import MyUser


# Create your views here.
def user_reg(request):
    if request.method == 'GET':
        form_obj = forms.UserRegForm()
        return render(request, 'shop/user_reg.html', {'form_obj': form_obj})
    if request.method == "POST":
        form_obj = forms.UserRegForm(request.POST, request.FILES)
        if form_obj.is_valid():
            uname = request.POST.get("username", '')
            users = MyUser.objects.filter(username=uname)
            if users:
                for user in users:
                    user_img = user.user_img
                info = '用户已经存在'
            else:
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
            print(errors)
            return render(request, "shop/user_reg.html", {'form_obj': form_obj, 'errors': errors})


def user_login(request):
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
