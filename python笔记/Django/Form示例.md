通过Form表单上传文件保存到模型ImgFile中

#### 1、路由

```python
    path('userimg/', views.imgfileform),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
```

#### 2、视图函数

```python
def imgfileform(request):
    if request.method == 'GET':
        f = ImgFileForm()
        return render(request, '5/upload_form.html', {'form_obj': f})
    else:
        f = ImgFileForm(data=request.POST, files=request.FILES)
        if f.is_valid():
            # print(f.clean())
            # {'name': '222', 'headimg': <InMemoryUploadedFile: 13315028795322919.png (image/png)>}
            name = f.cleaned_data['name']
            headimg = f.cleaned_data['headimg']
            # print(type(headimg)) #<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            userimg = ImgFile(name=name,headimg=headimg)
            # print(userimg)
            # userimg.name = name
            # userimg.heading = headimg
            userimg.save()
            # print(type(userimg)) #<class 'app5.models.ImgFile'>
            print('上传成功')
            return render(request, '5/upload_form.html', {"form_obj": f, 'user': userimg})
```

#### 3、模板

```html

<form enctype="multipart/form-data"  method="post">
    {% csrf_token %}
    {{ form_obj.as_p}}
    <br>
    <input type="submit" value="文件上传">
    <img src="/media/{{user.headimg}}">
</form>
```

#### 4、Form表单

```python
class ImgFileForm(forms.Form):
    name = forms.CharField()
    headimg = forms.FileField(label='头像')
```

#### 5、模型

```
class ImgFile(models.Model):
    name = models.CharField(verbose_name='用户名称',
                            default='',
                            max_length=30,
                            )
    headimg = models.FileField(verbose_name='文件名',
                               upload_to="uploads/", null=False, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '头像信息'
        db_table = 'user_img'
```

分析

```python

In [11]: userimg = ImgFile.objects.filter(id=47).get()

In [12]: type(userimg)
Out[12]: app5.models.ImgFile

In [13]: userimg.headimg
Out[13]: <FieldFile: uploads/WIN_20221202_19_18_16_Pro_OgsMHpS.jpg>

In [14]: print(userimg.headimg)
uploads/WIN_20221202_19_18_16_Pro_OgsMHpS.jpg

In [15]: dir(userimg)
Out[15]: 
['DoesNotExist',
 'MultipleObjectsReturned',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_check_column_name_clashes',
 '_check_constraints',
 '_check_default_pk',
 '_check_field_name_clashes',
 '_check_fields',
 '_check_id_field',
 '_check_index_together',
 '_check_indexes',
 '_check_local_fields',
 '_check_long_column_names',
 '_check_m2m_through_same_relationship',
 '_check_managers',
 '_check_model',
 '_check_model_name_db_lookup_clashes',
 '_check_ordering',
 '_check_property_name_related_field_accessor_clashes',
 '_check_single_primary_key',
 '_check_swappable',
 '_check_unique_together',
 '_do_insert',
 '_do_update',
 '_get_FIELD_display',
 '_get_expr_references',
 '_get_field_value_map',
 '_get_next_or_previous_by_FIELD',
 '_get_next_or_previous_in_order',
 '_get_pk_val',
 '_get_unique_checks',
 '_meta',
 '_perform_date_checks',
 '_perform_unique_checks',
 '_prepare_related_fields_for_save',
 '_save_parents',
 '_save_table',
 '_set_pk_val',
 '_state',
 'check',
 'clean',
 'clean_fields',
 'date_error_message',
 'delete',
 'from_db',
 'full_clean',
 'get_constraints',
 'get_deferred_fields',
 'headimg',
 'id',
 'name',
 'objects',
 'pk',
 'prepare_database_save',
 'refresh_from_db',
 'save',
 'save_base',
 'serializable_value',
 'unique_error_message',
 'validate_constraints',
 'validate_unique']

In [17]: userimg.__str__()
Out[17]: '3333'

In [18]: userimg.name
Out[18]: '3333'

In [19]: userimg.headimg.__str__
Out[19]: <bound method File.__str__ of <FieldFile: uploads/WIN_20221202_19_18_16_Pro_OgsMHpS.jpg>>

In [20]: userimg.headimg.__str__()
Out[20]: 'uploads/WIN_20221202_19_18_16_Pro_OgsMHpS.jpg'

In [21]: 

```

Django中froms表单使用日期选择器

```python
from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='昵称', max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.ChoiceField(label="密码", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    date = forms.DateField(label='日期', widget=forms.DateInput(attrs={'type':'date'}))
    #实现可选的日期输入格式

```

