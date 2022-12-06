# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/4 13:01
"""
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pageination import Pagination


# Create your views here.

def depart_list(request):
    """部门列表"""
    # 数据库总所有的部门信息
    queryset = models.Department.objects.all()
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, "depart_list.html", context)


def depart_add(request):
    """添加部门"""
    if request.method == "GET":

        return render(request, 'depart_add.html')
    # 获取用户通过post提交的数据

    """
    从表单中过来的请求头
    POST /depart/add/ HTTP/1.1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 118
    Content-Type: application/x-www-form-urlencoded
    Cookie: csrftoken=dl9GSKXeVMw4CgrTsKoHBn7M2TzOQDIe; sessionid=1yv8l67gyk9s188ihgjoens7njhs9cg9
    Host: 127.0.0.1:8000
    Origin: http://127.0.0.1:8000
    Pragma: no-cache
    Referer: http://127.0.0.1:8000/depart/add/
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: same-origin
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62
    sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    """
    title = request.POST.get('title')
    # print(request.POST)
    # < QueryDict: {'csrfmiddlewaretoken': ['Gx1wXzbNgeK4U9jvhcTdV7rcaEbL26CYJI02F9YR1Q6YmfAezM7KmkoO2nApIza2'],
    #               'title': ['11212']} >
    # 保存到数据库
    if models.Department.objects.filter(title=title):
        return render(request, 'error.html', {"error_msg": "此部门已经存在!"})
    models.Department.objects.create(title=title)
    # 重定向到部门列表
    return redirect('/depart/list/')


def depart_delete(request):
    """删除部门"""
    # assert isinstance(request.GET.get, object)
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()

        return render(request, 'depart_edit.html', {"row_object": row_object})
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")
