from django.shortcuts import render


# Create your views here.
def var(request):
    # 列表对象
    lists = ['Java', 'Python', 'C', 'C#', 'JavaScript']
    # 字典对象
    dicts = {
        '姓名': '张三',
        '年龄': 25,
        '性别': '男',
    }

    return render(request, '3/var.html', {'lists': lists, 'dicts': dicts})


def for_label(request):
    dict1 = {
        '书名': 'Django开发',
        '价格': 80,
        '作者': "张三",
    }
    dict2 = {
        '书名': 'Python开发',
        '价格': 90,
        '作者': "李四",
    }
    dict3 = {
        '书名': 'Java开发',
        '价格': 100,
        '作者': "王五",
    }
    lists = [dict1,dict2,dict3]
    return render(request,'3/for_label.html',{'lists':lists})


def welcome(request):
    return render(request,'3/welcome.html')