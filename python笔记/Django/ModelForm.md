

# ModelForm使用

## 1、定义模型：

```python
class Order(models.Model):
    """
    订单
    """
    oid = models.CharField(verbose_name='订单号',max_length=64)
    title = models.CharField(verbose_name='名称',max_length=32)
    price = models.IntegerField(verbose_name='价格')

    status_choices = (
        (1,'未支付'),
        (2,'已支付'),
    )
    status = models.SmallIntegerField(verbose_name='订单状态',choices=status_choices,default=1)
    admin = models.ForeignKey(verbose_name='管理员',to=Admin,on_delete=models.CASCADE)
```



## 2、定义模型表单

```python
class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中所有的字段，给每一个字段的插件设置
        for name, field in self.fields.items():
            # 字段中有属性，保留原来的属性。没有属性，才设置
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass
```



最简单的类：

```python
class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = "__all__"
        
        
```



## 3、视图函数：

```python
def order_list(request):
    form = OrderModelForm()
    context = {
        'form': form
    }
    return render(request, 'order_list.html', context)
```

## 4、模板：

```html
<form id="formAdd">
    <div class="clearfix">
        {% for field in form %}
        <div class="col-xs-6">
            <div class="form-group" style="position:relative;margin-bottom: 20px;">
                <label>{{ field.label }}</label>
                {{ field }}
   <span class="error-msg"  style="color: red;position: absolute">{{ field.errors.0 }}</span>
     </div>
         </div>
            {% endfor %}
    <button id="btnAdd" type="button" class="btn btn-primary">提交</button>
 </div>
                   </div>
  </form>
```

![image-20221210143734817](assets/image-20221210143734817-1670654263202-2.png)

## 更多用法：

### 排除某个字段。禁止将模型字段转换为表单字段，用法同fields

```python
class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ['oid',]
        
```

![image-20221210144128654](assets/image-20221210144128654.png)

labels 设置表单字段的label项，以字典方式表示，字典的键为模型的字段

```python
class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ['oid']
        labels = {
            "title": "订单名称",
            "price": '商品价格'
        }
```

![image-20221210144337768](assets/image-20221210144337768.png)

#### 错误信息

```python
class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ['oid']
        labels = {
            "title": "订单名称",
            "price": '商品价格'
        }
        error_messages = {
            'title': {'required':"订单名称不能为空！"},
            'price':{'required':'价格不能为空!'},
            'admin':{'required':'管理员不能为空!'}
        }
```

##### 修改后的错误信息

![image-20221210155651734](assets/image-20221210155651734.png)

##### 默认的错误信息

![image-20221210155735563](assets/image-20221210155735563.png)

#### 遍历form

```python
    form = UserBaseInfoModelForm()
    print(type(form))
    for item in form:
        print(item)
        print(type(item))
```

```python

<class 'app5.forms.UserBaseInfoModelForm'>
<input type="text" name="username" maxlength="30" required id="id_username">
<class 'django.forms.boundfield.BoundField'>
<input type="password" name="password" class="password" maxlength="20" required id="id_password">
<class 'django.forms.boundfield.BoundField'>
<input type="text" name="status" maxlength="1" required id="id_status">
<class 'django.forms.boundfield.BoundField'>
<input type="text" name="createdate" required id="id_createdate">
<class 'django.forms.boundfield.BoundField'>
[13/Dec/2022 19:08:18] "GET /user/add/ HTTP/1.1" 200 801

```

#### 处理模型表单数据

提供了save方法，用于将表单绑定的数据直接保存到数据库中。

###### 1、接受POST请求提交的数据，直接保存到数据库中，返回一个模型对象。

```python
f = UserInfoBaseModelForm(request.POST)
new_userinfo = f.save()
```

###### 2、调用表单类生成类实例，完成数据显示

```python
a = UserInfoBaseModel.objects.get(id=1)
f = UserBaseModelForm(instance=a)
```

###### 3、调用表单类生成实例，完成数据修改

```python
a = UserInfoBaseModel.objects.get(id=1)
f = UserInfoBaseModelForm(request.POST,instance = a)
new_userinfo = f.save()
```

