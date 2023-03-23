from django.shortcuts import HttpResponse, render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from apps.ajax.models import Type, TypeDetail


def init(request):
    type = Type.objects.all()
    return render(request, 'ajax.html', {'type': type})


def find_type(request):
    """获取具体类型"""

    # 获取传回来的数据
    type_id = request.GET.get('type_id')
    # 从数据库筛选出符合条件的数据，根据自己的需求更换
    type_detail = TypeDetail.objects.filter(type_id=type_id)
    # 将queryset转换成json
    shop_type_detail = serializers.serialize("json", type_detail)
    return HttpResponse(shop_type_detail)

# @csrf_exempt
# def find_type(request):
#     type_id = request.GET.get('type_id')
#     shop_type_detail = serializers.serialize("json", TypeDetail.objects.filter(type_id=type_id))
#     return HttpResponse(shop_type_detail)

