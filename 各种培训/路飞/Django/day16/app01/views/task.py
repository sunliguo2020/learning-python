# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/6 15:16
"""
import json

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app01.utils.form import TaskModelForm
from app01 import models
from app01.utils.pageination import Pagination


def task_list(request):
    """任务列表"""
    # 去数据库获取所有的任务
    queryset = models.Task.objects.all().order_by('-id')
    page_object = Pagination(request,queryset,page_size=5)
    form = TaskModelForm()
    context = {
        "form": form,
        'queryset': page_object.page_queryset,
        'page_string':page_object.html()
    }
    return render(request, 'task_list.html', context)


@csrf_exempt
def task_ajax(request):
    # GET /task/ajax/?n1=123&n2=456 HTTP/1.1
    # <QueryDict: {'n1': ['123'], 'n2': ['456']}>
    print(request.GET)
    # [06/Dec/2022 16:56:10] "POST /task/ajax/ HTTP/1.1" 200 9
    # <QueryDict: {'n1': ['123'], 'n2': ['456']}>
    """
    POST /task/ajax/ HTTP/1.1
    Host: 127.0.0.1:8000
    Connection: keep-alive
    Content-Length: 13
    Pragma: no-cache
    Cache-Control: no-cache
    sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
    Accept: */*
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    sec-ch-ua-mobile: ?0
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62
    sec-ch-ua-platform: "Windows"
    Origin: http://127.0.0.1:8000
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: http://127.0.0.1:8000/task/list/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
    Cookie: csrftoken=dl9GSKXeVMw4CgrTsKoHBn7M2TzOQDIe; sessionid=1yv8l67gyk9s188ihgjoens7njhs9cg9
    
    n1=123&n2=456HTTP/1.1 200 OK
    Date: Tue, 06 Dec 2022 08:35:16 GMT
    Server: WSGIServer/0.2 CPython/3.11.0
    Content-Type: text/html; charset=utf-8
    X-Frame-Options: DENY
    Content-Length: 9
    Vary: Cookie
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    成功了
    """

    print(request.POST)
    data_dict = {'status': True, 'data': [11, 22, 33, 44]}
    # json_string = json.dumps(data_dict)
    # return HttpResponse(json_string)
    return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    print(request.POST)
    # <QueryDict: {'lvevel': ['1'], 'title': ['dsfdsf'], 'detail': ['sss'], 'user': ['8']}>

    # 1、用户发送过来的数据进行表单校验。
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status': True}
        return HttpResponse(json.dumps(data_dict))
    # print(type(form.errors))
    # <class 'django.forms.utils.ErrorDict'>
    data_dict = {'status': False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict))
