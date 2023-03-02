from apps.goods.models import *
from django import forms
from django.core.exceptions import ValidationError
import re
from apps.goods.views import *


def sort_validate(value):
    sort_re = re.compile(
        r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not sort_re.match(value):
        raise ValidationError('排序必须为正整数')


class GoodsCategoryForm(forms.Form):
    name = forms.CharField(label="分类名称", min_length=2,
                           widget=forms.widgets.TextInput(
                               attrs={'class': 'form-control', 'placeholder': "请输入分类名称"}),
                           error_messages={
                               'required': '分类名称不能为空',
                               'min_length': '长度最少2位',
                           })
    parent_id = forms.CharField(label="选择父类", max_length=20, required=True,
                                widget=forms.widgets.Select(
                                    attrs={'class': 'form-control custom-select', 'placeholder': "请选择父类"}),
                                error_messages={
                                    'required': '请选择父类',
                                })

    sort = forms.CharField(label="排序",
                           widget=forms.widgets.TextInput(
                               attrs={'class': 'form-control', 'placeholder': "请输入数字"}),
                           error_messages={
                               'required': '排序值不能为空',
                           })
    logo = forms.ImageField(label="分类图片", required=False, widget=forms.widgets.FileInput(
        attrs={'class': 'custom-file-input'}))

    def __init__(self, *args, **kwargs):

        super(GoodsCategoryForm, self).__init__(*args, **kwargs)
        cates_all = GoodsCategory.objects.all()
        self.alist = [('', '请选择...')]
        self.fields['parent_id'].widget.choices = self.binddata(cates_all, 0, 1)

    def binddata(self, datas, id, n):
        if id == 0:
            datas = datas.filter(parent__isnull=True)
        else:
            datas = datas.filter(parent_id=id)
        for data in datas:
            # 列表中添加元组
            self.alist.append((data.id, self.spacelength(n) + data.name))
            # 递归处理
            self.binddata(datas, data.id, n + 2)
        return self.alist

    def spacelength(self, i):
        space = ''
        for j in range(1, i):
            space += "--"
        return space + "|--"
