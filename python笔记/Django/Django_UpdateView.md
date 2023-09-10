Django之UpdateView

模型



```python
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse

class AdvPosition(BaseModel):
    name = models.CharField(max_length=255, help_text = "广告位名称")
    def get_absolute_url(self):
        return reverse('backend:adv-position-index')

    class Meta(BaseModel.Meta):
        db_table =  'adv_position'
```
模型中需要设定跳转地址，在保存成功后会根据这个地址跳转。

####  url

```python
path('adv-position/update/<int:pk>', AdvPositionUpdateView.as_view(), name = 'adv-position-update'),
```



由于model使用了app_name

所以需要再urls.py中添加

```python
app_name = 'backend'
```

#### update.html

```html

<form class="form-horizontal" action="{{ request.get_full_path }}" method="post">
    {% csrf_token %}
   
  <div class="card-body">
    {{ form.as_ul }}
  </div>
  <div class="card-footer">
    <input type="submit" class="btn btn-info" value="submit" />
  </div>

```



#### view

跟CreateView一样，UpdateView也有很多中方式

#### 方式1：定义类变量 fields

```python
class AdvPositionUpdateView(UpdateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/update.html'
    fields = ['name']
```



#### 方式2：定义ModelForm类

```python
from django import forms 
from common.models import AdvPosition

class AdvPositionForm(forms.ModelForm):
    class Meta:
        model = AdvPosition
        fields = ['name']
```



```python
class AdvPositionUpdateView(UpdateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/update.html'
    form_class = AdvPositionForm
```



#### 方式3：使用get，post

```python

class AdvPositionUpdateView(UpdateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/update.html'
    form_class = AdvPositionForm	
    
    def get(self, request, *args, **kwargs):
        adv_positin = AdvPosition.objects.get(id = self.kwargs['pk'])
        #initial = {'name': adv_positin.name}
        #form = self.form_class(initial)
        form = self.form_class(instance=adv_positin)
        return render(request, 'adv-position/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        adv_positin = AdvPosition.objects.get(id = self.kwargs['pk'])
        adv_positin.name = request.POST.get('name')
        adv_positin.save()
        return redirect('/backend/adv-position/index')
```
这里注意的是，我们需要给表单初始化已有数据

有种方式

instance和initial

form = self.form_class(instance=adv_positin)
adv = get_object_or_404(AdvPosition, pk=kwargs['pk'])
initial = {'name': adv.name}
form = self.form_class(initial)

#### 方式4：



```python
class AdvPositionUpdateView(UpdateView):
    model = AdvPosition # 指定模型
    template_name = 'adv-position/update.html'
    def get(self, request, *args, **kwargs):
        adv_positin = AdvPosition.objects.get(id = self.kwargs['pk'])
        #initial = {'name': adv_positin.name}
        #form = AdvPositionForm(initial)
        form = AdvPositionForm(instance=adv_positin)
        return render(request, 'adv-position/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        adv_positin = AdvPosition.objects.get(id = self.kwargs['pk'])
        adv_positin.name = request.POST.get('name')
        adv_positin.save()
        return redirect('/backend/adv-position/index')
```

