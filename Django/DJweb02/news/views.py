from django.http import HttpResponse

from .models import NewsInfo


# Create your views here.


def index(request):
    return HttpResponse('这是index返回的数据')


def news_list(request):
    """返回新闻列表"""
    # 获取newinfo这个表中的所有树
    # 下面的代码等同于执行sql: select * from newinfo
    datas = NewsInfo.objects.all()
    # 遍历查询到的所有数据
    result = ''
    for item in datas:
        # 获取新闻的标题
        title = f'<h1>{item.title}</h1>'
        result += title

    return HttpResponse(result)
