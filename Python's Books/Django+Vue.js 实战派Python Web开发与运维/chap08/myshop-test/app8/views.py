import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Goods
from .serializers import GoodsSerializer


# Create your views here.
class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:20]
        for good in goods:
            json_dict = {'name': good.name,
                         # Object of type Decimal is not JSON serializable
                         'market_price': good.market_price.to_eng_string()}

            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list, ensure_ascii=False, indent=4),
                            content_type="application/json")


class GoodsListViewJsonResponse(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:20]
        for good in goods:
            json_dict = {'name': good.name,
                         'market_price': good.market_price.to_eng_string()}
            json_list.append(json_dict)

        return JsonResponse(json_list,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False, "indent": 4},
                            # content_type="application/json"
                            )


class GoodsView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取queryset
        goods = Goods.objects.all()[:10]
        # 开始序列化多条数据，加上many=True
        # 对于GoodsSerializer类的many参数，如果传入的是QuerySet对象，则将器设置为True
        # 如果传入的是模型类，则将其设置为Flase。
        goods_json = GoodsSerializer(goods, many=True)
        # goods_json = GoodsSerializer(Goods)

        # goods_json = GoodsModelSerializer(goods, many=True)
        # 返回序列化对象。goods_json.data 是序列化后的值
        # OrderedDict([('name', '哈密大枣'), ('market_price', '69.00'), ('price', '59.00')]),
        print(goods_json.data)

        return Response(goods_json.data)
