from django.views.generic import View,ListView,DetailView
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'article/index.html')


class IndexView(View):
    def get(self,request):
        return render(request,'article/index.html')
    def post(self,request,*args, **kwargs):
        return render(request)
    
class BaykeArticleListView(ListView):
    template_name = 'article/list.html'
    context_object_name = 'article_list'
    queryset = [i for i in range(1,20)]


class BaykeArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    context_object_name = 'article'
    queryset = []