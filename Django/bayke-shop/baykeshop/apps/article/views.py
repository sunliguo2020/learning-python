from django.views.generic import View
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'article/index.html')


class IndexView(View):
    def get(self,request):
        return render(request,'article/index.html')
    def post(self,request,*args, **kwargs):
        return render(request)