import json

from django.http import HttpResponse
from django.views import View

from .models import Goods


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
