from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import EmailVerifyRecord
from .models import UserProfile  # 引入用户模型字段

# Create your views here.

class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):   # 加密明文密码
                return user
        except Exception as e:
            return None


def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    if request.method == 'POST':   # 判断采用的是何种请求

        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        user = authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if user is not None:
            # login方法登录
            login(request, user)
            # 返回登录成功信息
            return HttpResponse('登陆成功')
        else:
            # 返回登录失败信息
            return HttpResponse('账号或者密码错误')
    return render(request,'users/login.html',{'form':form})

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
      
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
             # 让username等于邮箱即可
            new_user.username = form.cleaned_data.get('email')  
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return redirect('users:login')
        
    context = {
            'form':form
        }
    print(form)
    return render(request, 'users/register.html', context)
    
def active_user(request, active_code):
    """查询验证码"""
    print(active_code)
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    print(all_records)
    if all_records:
        for record in all_records:
            email = record.email
            print(email)
            user = User.objects.get(email=email)
            print(user)
            user.is_staff = True
            user.save()
    else:
        return HttpResponse('链接有误！')
    return redirect('users:login')


@login_required(login_url='users:login')   # 设置登录后才能访问，如果没有登陆，就跳转到登录界面
def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'users/user_profile.html', {'user': user})

def logout_view(request):
    logout(request=request)
    return redirect('users:login')

