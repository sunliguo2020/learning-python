# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/3 21:41
自定义分页组件,以后如果想要使用这个分页组件，你需要做一下几件事：

在视图函数中：
    def prettynum_list(request):

       #1、根据自己的情况去筛选数据
        query_set = models.PrettyNum.objects.all()
        #2、实例化实例对象
        page_object = Pagination(request, query_set)

        context = {
                    "query_set": page_object.page_queryset,#分完页的数据
                   "page_string": page_object.html()#生成页码
                   }

        return render(request, "prettypnum_list.html", context)

在HTML页面中
    {% for obj in query_set %}
        {{obj.xxx}}
    {% endfor %}

     <div class="clearfix" >
                <ul class="pagination">
                 {{ page_string }}
                </ul>
    </div>

"""
import copy
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, plus=5, page_param='page', ):
        """

        :param request:请求的对象
        :param queryset:查询符合条件的数据
        :param page_size: 每页多少条
        :param plus:显示当前页前几页或后几页
        :param page_param:在url中传递的获取分页的参数，例如：/?page=
        """

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        # print(query_dict)
        self.query_dict = query_dict
        # query_dict.setlist['page',[11]]
        # print(query_dict.urlencode())
        page = request.GET.get(page_param, "1")

        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        # 当前页
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        self.page_param = page_param

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, self.page_size)
        if div:
            total_page_count += 1

        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):

        # 计算出当前显示的前5页和后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库内容比较少
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页>5
                # 当前页+5>总页数
                if self.page + self.plus > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append(f'<li ><a href="?{self.query_dict.urlencode()}">首页</a></li>')
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = f'<li ><a href="?{self.query_dict.urlencode()}">上一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = f'<li ><a href="?{self.query_dict.urlencode()}">上一页</a></li>'

        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = f'<li class="active"><a href="?{self.query_dict.urlencode()}">{i}</a></li>'
            else:
                ele = f'<li><a href="?{self.query_dict.urlencode()}">{i}</a></li>'
            page_str_list.append(ele)

        # 下一页
        if self.page + 1 <= self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = f'<li ><a href="?{self.query_dict.urlencode()}">下一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = f'<li ><a href="?{self.query_dict.urlencode()}">下一页</a></li>'

        page_str_list.append(prev)
        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append(f'<li ><a href="?{self.query_dict.urlencode()}">尾页</a></li>')

        search_string = """
        <li>
            <form style="float:left;margin-lef:-1px" method="get">
                <input style="postion:relative;float:left;display:inline-block;width: 80px;border-radius: 0;"
                           type="text" name="page" class="form-control" placeholder="页码">
                <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
            </form>
        </li>
        """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))

        return page_string
