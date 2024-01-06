import json

from django.http import HttpResponse


# Create your views here.

def users(requests):
    user_list = ['alex', 'oldboy'
                 ]
    return HttpResponse(json.dumps(user_list))


from django.views import View


class StudentsView(View):
    def dispatch(self, request, *args, **kwargs):
        print(request.method)
        func = getattr(self, request.method.lower())
        ret = func(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST; ')

    def put(self, request, *args, **kwargs):
        return HttpResponse('put')
