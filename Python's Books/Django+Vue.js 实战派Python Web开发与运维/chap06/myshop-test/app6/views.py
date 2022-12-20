from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def user_reg(request):
    if request.method == 'GET':
        return render(request, '6/user_reg.html')
    if request.method == 'POST':
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        re_pwd = request.POST.get('re-password')
        print('uname=', uname)
        if pwd != re_pwd:
            info = '密码和重复密码不一样'
        else:
            if User.objects.filter(username=uname):
                info = '用户已经存在'
            else:
                d = dict(username=uname,
                         password=pwd,
                         email='111@111.com',
                         is_staff=1,
                         is_active=1,
                         is_superuser=1)
                print(d)
                user = User.objects.create_user(**d)
                info = '注册成功，请登录'
        return render(request, '6/user_reg.html', {'info': info})


