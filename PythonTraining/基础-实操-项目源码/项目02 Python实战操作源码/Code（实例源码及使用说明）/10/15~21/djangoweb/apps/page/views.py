from django.shortcuts import render
from django.views.generic import View
# 引入Paginator
from django.core.paginator import Paginator

# 引入的模型，需根据需求变换
from apps.mail.models import User


class IndexView(View):
    """数据分页显示"""

    def get(self, request, page):
        """分页显示"""

        # 根据业务需求从数据库里查询出数据

        shop_info = User.objects.all()
        # 对数据进行分页
        paginator = Paginator(shop_info, 1)  # 10表示每页显示10条
        # 获取第page页的内容，默认为第一页
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1
        # 获取第page页的Page实例对象
        shop_page = paginator.page(page)
        # 进行页码的控制，页面上最多显示5个页码
        # 1.总页数小于5页，页面上显示所有页码
        # 2.如果当前页是前3页，显示1-5页
        # 3.如果当前页是后3页，显示后5页
        # 4.其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        # 构造数据并返回
        context = {'shop_page': shop_page, 'pages': pages}
        return render(request, 'page.html', context)
