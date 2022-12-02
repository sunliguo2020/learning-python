from django.shortcuts import render, redirect
from app01 import models


# Create your views here.

def depart_list(request):
    """部门列表"""
    # 数据库总所有的部门信息
    queryset = models.Department.objects.all()
    return render(request, "depart_list.html", {"queryset": queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取用户通过post提交的数据
    title = request.POST.get('title')
    # 保存到数据库
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


def user_list(request):
    """用户管理"""

    query_set = models.UserInfo.objects.all()
    for obj in query_set:
        print(obj.id,obj.name)
    return render(request,'user_list.html',{"user_list":query_set})