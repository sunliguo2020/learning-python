from django.shortcuts import render

import json
# Create your views here.


class GoodsListView(view):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:20]
        for good in Goods:
            json_dict = {}
            json_dict['name'] = good.name

            json_list.append(json_dict)

        return HtttpResponse(json.dumps(json_list, ensure_ascii=False, indent=4), content_type="application/json")
