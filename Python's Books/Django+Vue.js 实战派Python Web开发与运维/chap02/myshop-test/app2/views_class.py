# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 11:26
"""
from django.views.generic import TemplateView


class TestTemplateVies(TemplateView):
    # 设置模板文件
    template_name = '2/test_templateview.html'

    # 重写父类的get_context_data()方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context['info'] = '该变量可以传递到模板'
        return context
