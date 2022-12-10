# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 13:03
"""
import datetime
import random

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app01.utils.form import OrderModelForm
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from app01.utils.pageination import Pagination


def order_list(request):
    query_set = models.Order.objects.all().order_by('-id')
    page_object = Pagination(request, query_set)

    form = OrderModelForm()
    context = {
        'form': form,
        'queryset': page_object.page_queryset,
        "pagestring": page_object.html(),
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """
    创建订单
    :param request:
    :return:
    """

    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # print(form)
        """<tr>
    <th><label for="id_title">订单名称:</label></th>
    <td>
      
      <input type="text" name="title" value="qw" maxlength="32" class="form-control" placeholder="订单名称" required id="id_title">
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_price">商品价格:</label></th>
    <td>
      
      <input type="number" name="price" value="3333" class="form-control" placeholder="商品价格" required id="id_price">
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_status">订单状态:</label></th>
    <td>
      
      <select name="status" class="form-control" placeholder="订单状态" id="id_status">
  <option value="1" selected>未支付</option>

  <option value="2">已支付</option>

</select>
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_admin">管理员:</label></th>
    <td>
      
      <select name="admin" class="form-control" placeholder="管理员" required id="id_admin">
  <option value="">---------</option>

  <option value="1" selected>sunliguo</option>

  <option value="2">root</option>

</select>
      
      
        
      
    </td>
  </tr>
        
        """
        # print(type(form))
        # <class 'app01.utils.form.OrderModelForm'>
        # print(form.cleaned_data)
        # {'title': 'qw', 'price': 3333, 'status': 1, 'admin': <Admin: sunliguo>}

        # 用户没有提交的数据
        form.instance.oid = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

        # 管理员没有输入
        # django.db.utils.IntegrityError: (1048, "Column 'admin_id' cannot be null")
        form.instance.admin_id = request.session['info']['id']
        # 保存到数据库
        form.save()
        return JsonResponse({"status": True})
        # return HttpResponse(json.dumps({"status":True}))
    else:
        return JsonResponse({'status': False, 'error': form.errors})
        '''
        error: {title: ["这个字段是必填项。"], price: ["这个字段是必填项。"], admin: ["这个字段是必填项。"]}
        status: false
        '''


def order_delete(request):
    if request.method == "GET":
        uid = request.GET.get('uid')
        # print('uid=', uid)
        if not uid:
            return JsonResponse({"status": False, 'error': '参数有误!'})
        exist = models.Order.objects.filter(id=uid).exists()
        # print('exist=', exist)
        if not exist:
            return JsonResponse({"status": False, 'error': "此id不存在!"})

        models.Order.objects.filter(id=uid).delete()

    return JsonResponse({"status": True})
