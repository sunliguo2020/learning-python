from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, '1/index.html')  # 将渲染结果输出到index.html模板中
