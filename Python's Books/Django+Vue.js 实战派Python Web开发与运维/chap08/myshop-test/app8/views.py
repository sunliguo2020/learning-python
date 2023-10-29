import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods
from .serializers import GoodsSerializer, GoodsModelSerializer


# Create your views here.


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:20]
        for good in Goods:
            json_dict = {}
            json_dict['name'] = good.name

            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list, ensure_ascii=False, indent=4), content_type="application/json")


class GoodsListView_JsonResponse(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:20]
        for good in Goods:
            json_dict = {}
            json_dict['name'] = good.name

            json_list.append(json_dict)

        return JsonResponse(json_list,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False, "indent": 4},
                            content_type="application/json")


class GoodsView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取queryset
        goods = Goods.objects.all()[:10]
        # 开始序列化多条数据，加上many=True
        goods_json = GoodsSerializer(goods, many=True)
        goods_json = GoodsModelSerializer(goods,many=True)
        # 返回序列化对象。goods_json.data 是序列化后的值
        print(goods_json.data)

        return Response(goods_json.data)
