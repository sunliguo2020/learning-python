from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View

from .models import UserBaseInfo


# Create your views here.
def index(request):
    return HttpResponse('app2中的index方法')


def show(request, id):
    return HttpResponse("app2中的show方法,参数为id，值为" + str(id))


def show_uuid(request, id):
    return HttpResponse("app2中的show_uuid方法,参数为id,值为" + str(id))


def show_slug(request, q):
    return HttpResponse("app2中的show_slug方法，参数为q，值为" + str(q))


def article_list(request, year):
    return HttpResponse("app2中的article_list方法,参数为year，指定为4位数，值为" + str(year))


def url_reverse(request):
    # 使用reverse()方法反向解析
    print("在views()函数中使用reverse()解析出的结果为：" + str(reverse("app2_url_reverse")))
    return render(request, "2/url_reverse.html")


def hello(request):
    string = f",{request.path},{request.method},{request.user},{request.META}"
    return HttpResponse("Hello Django!!!" + str(string))


def test_get(request):
    print(request.get_host())
    # print(request.get_raw_uri())
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.GET)
    print(request.META["HTTP_USER_AGENT"])
    print(request.META["REMOTE_ADDR"])
    print(request.GET.get('username'))

    return HttpResponse("")


def test_render(request):
    context = {
        'info': 'hello django',
    }
    return render(request, '2/test_render.html', context, content_type='text/html')


def test_redirect_model(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)


def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse('编号：' + str(user.id) + "姓名：" + user.username)


class IndexPageView(View):
    '''
    类视图
    '''

    def get(self, request):
        return HttpResponse('GET请求')

    def post(self, request):
        return HttpResponse('POST请求')
