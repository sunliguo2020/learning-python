# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View

from apps.goods.forms import GoodsCategoryForm,GoodsModelForm
from apps.goods.models import *


class GoodsCategoryView(View):
    def get(self, request):
        cates = GoodsCategory.objects.all()
        return render(request, "shop/goods/cate_index.html", {"cates": cates})

    def post(self, request):
        pass


class GoodsCategoryAddView(View):
    def __init__(self):
        self.alist = {}

    def binddata(self, datas, id, n):
        if id == 0:
            datas = datas.filter(parent__isnull=True)
        else:
            datas = datas.filter(parent__isnull=True)
        for data in datas:
            self.alist[data.id] = self.spacelength(n) + data.name
            self.binddata(datas, data.id, n + 2)
        return self.alist

    def spacelength(self, i):
        space = ''
        for j in range(1, i):
            space += "&nbsp;&nbsp;"
        return space + "|--"

    def get(self, request):
        form_obj = GoodsCategoryForm()
        return render(request, "shop/goods/cate_add.html", {"form_obj": form_obj,'title':'商品分类新增'})

    def post(self, request):
        form_obj = GoodsCategoryForm(request.POST, request.FILES)
        if form_obj.is_valid():
            name = request.POST.get("name", '')
            cates = GoodsCategory.objects.filter(name=name)
            if cates:
                info = '分类已经存在'
            else:
                # form_obj.cleaned_data["is_staff"]=1
                # form_obj.cleaned_data["is_superuser"]=0 #非管理员
                # 接收页面传递过来的参数，进行新增
                cate = GoodsCategory.objects.create(**form_obj.cleaned_data)
                # 成功后，重定向到商品分类列表页面
                # info='注册成功,请登陆'
                return redirect('cate_index')
            return render(request, 'shop/goods/cate_index.html', {"form_obj": form_obj, "info": info})
        else:
            errors = form_obj.errors
            print(errors)
            return render(request, "shop/goods/cate_add.html", {'form_obj': form_obj, 'info': errors})


class GoodsView(View):
    def __init__(self):
        self.alist = {}

    def binddata(self, datas, id, n):
        datas = GoodsCategory.objects.filter(parent_id=id)
        for data in datas:
            self.alist[data.id] = self.spacelength(n) + data.name
            self.binddata(datas, data.id, n + 2)
        return self.alist

    def spacelength(self, i):
        space = ''
        for j in range(1, i):
            space += "&nbsp;&nbsp;"
        return space + "|--"

    def get(self, request):
        # goods = Goods.objects.all()
        # cates = self.binddata(cates_all, 0, 1)
        return render(request, "shop/goods/index.html")

    def post(self, request):
        pass


class GoodsAddView(View):
    def __init__(self):
        self.alist = {}

    def binddata(self, datas, id, n):
        if id == 0:
            datas = GoodsCategory.objects.filter(parent__isnull=True)
        else:
            datas = GoodsCategory.objects.filter(parent_id=id)
        for data in datas:
            self.alist[data.id] = self.spacelength(n) + data.name
            self.binddata(datas, data.id, n + 2)
        return self.alist

    def spacelength(self, i):
        space = ''
        for j in range(1, i):
            space += "&nbsp;&nbsp;"
        return space + "|--"

    def get(self, request):
        cates_all = GoodsCategory.objects.all()
        cates = self.binddata(cates_all, 0, 1)
        goods_obj = GoodsModelForm()
        return render(request, "shop/goods/add.html", {"cates": cates,'form_obj':goods_obj})

    def post(self, request):
        goods_form = GoodsModelForm(data=request.POST)
        if goods_form.is_valid():
            goods_form.save()
            return redirect(reverse('goods_index'))
        else:
            errors = goods_form.errors
            return render(request,'shop/goods/add.html',{'form_obj':goods_form,'errors':errors})
        return render(request,'shop/goods/add.html',{'form_obj':goods_form})

def ajax_goods(request):
    cate_id = request.GET.get("cate_id", '')
    goodname = request.GET.get("goodname", '')
    status = request.GET.get("status")

    search_dict = dict()
    if cate_id:
        search_dict["category"] = cate_id
    if goodname:
        search_dict["name__contains"] = goodname
    if status:
        search_dict["status"] = status

    page_size = 2
    page = int(request.GET["page"])
    # 获取总数count
    total = Goods.objects.filter(**search_dict).count()
    # print(**search_dict)
    # 通过切片获取当前页和下一页的数据
    goods = Goods.objects.filter(**search_dict).order_by("-id")[(page - 1) * page_size: page * page_size]
    rows = []
    datas = {"total": total, "rows": rows}
    for good in goods:
        rows.append({
            "id": good.id,
            "name": good.name,
            "market_price": good.market_price,
            "price": good.price,
            "category_id": good.category.name,
            "click_num": good.click_num,
            "amount": good.amount,
        })
    return JsonResponse(datas, safe=False, json_dumps_params={'ensure_ascii': False, "indent": 4})
