from django.shortcuts import render, HttpResponse, redirect


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
    roles = ['管理员', 'CEO', '保安']
    user_info = {"name": "果汁",
                 "salary": 1000,
                 "role": "CTO",
                 }
    return render(request, 'tpl.html', {"a1": name, "a2": roles, "a3": user_info})


def news(request):
    # 1、定义一些新闻   网络请求联通新闻
    chinaunicom_news_url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/4/2022/11/news"

    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    req = requests.get(chinaunicom_news_url, headers=headers)
    print(req.json())
    data_list = req.json()
    # print(data_list)
    return render(request, 'news.html', {'news': data_list})


def something(request):
    # 1、获取请求方式  GET POST
    print(request.method)
    # 2、在url上传递参数 /something/?n1=d11&n2=2222
    print(request.GET)
    # 3、在请求体中获取数据
    print(request.POST)
    # 4、【相应】HttpResponse("返回内容") ,内容字符串内容发回给请求者。
    # return HttpResponse('返回内容')
    # 5、【相应】读取HTML内容+渲染（替换）->字符串，返回给浏览器
    # return render(request,"someting.html",{"title":"来了"})
    # 6、【相应】 redirect 让浏览器重定向
    return redirect("http://blog.sunliguo.com")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 用户post请求
        """<QueryDict: {'csrfmiddlewaretoken': ['yqXuI23rNzIvOpUuLWqcm7XbXVY668IXrHZcvjW4OD0pdLF9h3D5b1hkTozZFyH0'],
         'user': ['ll_admin'], 
         'pwd': ['tongmingao']}>"""

        print(request.POST)
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if username == 'root' and pwd == '123':

            return HttpResponse('登录成功!')
        else:
            return render(request, 'login.html', {"err_msg": "用户名或密码错误!"})


from app01 import models


def orm(request):
    # 新建数据
    models.Department.objects.create(title='销售部')
    # 删除数据
    models.Department.objects.filter(id=1).delete()
    models.Department.objects.all().delete()
    # 获取数据
    data_list = models.UserInfo.objects.all()
    print(data_list)
    for item in data_list:
        print(item.id, item.name)
    # 更新数据
    models.UserInfo.objects.filter(id='1').update(age=19)
    return HttpResponse('成功')
