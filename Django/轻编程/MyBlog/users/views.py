from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm
# Create your views here.

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
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            return redirect('users:login')
        
    context = {
            'form':form
        }
    print(form)
    return render(request, 'users/register.html', context)
    
