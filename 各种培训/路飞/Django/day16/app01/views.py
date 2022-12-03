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
    # for obj in query_set:
    #     print(obj.id, obj.name)
    return render(request, 'user_list.html', {"user_list": query_set})


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        content = {
            "gender_choice": models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all(),

        }

        return render(request, 'user_add.html', content)
    # 获取用户提交的数据
    name = request.POST.get('name')
    age = request.POST.get('age')
    pwd = request.POST.get('pwd')
    ac = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gd = request.POST.get('gd')
    dp = request.POST.get('dp')
    # 添加到数据库中
    models.UserInfo.objects.create(name=name,
                                   password=pwd,
                                   age=age,
                                   account=ac,
                                   create_time=ctime,
                                   gender=gd,
                                   dpart_id=dp)
    return redirect('/user/list/')


def user_delete(request, nid):
    """"删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")


from django import forms


class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, label='用户名')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'dpart']

        widgets = {
            "name": forms.TextInput(attrs={'class': "form-control"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(type(field))
            # print(name, field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_model_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == 'GET':
        form = UserModelForm()

        return render(request, 'user_model_form_add.html', {'form': form})
    # 用户POST提交的数据
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    else:  # 校验失败，显示错误信息
        return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_obj)
        return render(request, 'user_edit.html', {"form": form})

    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        # 默认保存的是用户输入的所有的数据，如果想要在用户输入意外增加值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')

    return render(request, 'user_edit.html', {'form': form})
