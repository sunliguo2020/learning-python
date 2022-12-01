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
    roles = ['管理员','CEO','保安']
    user_info = {"name":"果汁",
                 "salary":1000,
                 "role":"CTO",
                 }
    return render(request, 'tpl.html', {"a1": name,"a2":roles,"a3":user_info})

def news(request):
    #1、定义一些新闻   网络请求联通新闻
    chinaunicom_news_url = "http://www.chinaunicom.com.cn/api/article/NewsByIndex/4/2022/11/news"

    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    req = requests.get(chinaunicom_news_url,headers=headers)
    print(req.json())
    data_list = req.json()
    # print(data_list)
    return render(request,'news.html',{'news':data_list})
