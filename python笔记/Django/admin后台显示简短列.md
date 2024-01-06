
在 Django 的管理后台中显示 `JSONField` 可以采取以下方法，以便以更整洁的方式展示数据：

### 1. 自定义 Admin 模型的 `list_display` 属性

```
pythonCopy codefrom django.contrib import admin
from .models import HisInformation

@admin.register(HisInformation)
class HisInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'idcard', 'year', 'shortened_data',)  # Add 'shortened_data' to list_display

    def shortened_data(self, obj):
        # Display a shortened version of the data field
        data_str = str(obj.data)
        return data_str[:50] + '...' if len(data_str) > 50 else data_str  # Display first 50 characters

    shortened_data.short_description = 'Shortened Data'  # Set the column header in the admin interface
```

在这个示例中，`shortened_data` 方法用于在管理后台显示 `JSONField` 字段的缩短版本。`list_display` 中添加了 `shortened_data` 字段来显示缩短后的数据。你可以根据需要更改 `50` 这个数字来适应你希望在管理后台显示的字符数。

### 2. 使用自定义模板渲染字段

创建一个自定义的 Admin 模板来呈现数据字段。在你的应用程序目录下创建 `templates` 文件夹，然后创建一个与模型名对应的文件夹，再创建一个名为 `change_list.html` 的文件。

```
htmlCopy code<!-- templates/your_app_name/hisinformation/change_list.html -->
{% extends "admin/change_list.html" %}

{% load i18n %}

{% block result_list %}
    {% for item in result_list %}
        <tr class="{% cycle 'row1' 'row2' %}">
            <td>{{ item.id }}</td>
            <td>{{ item.idcard }}</td>
            <td>{{ item.year }}</td>
            <td>{{ item.data|truncatechars:50 }}</td>  <!-- Display a truncated version of the data field -->
        </tr>
    {% endfor %}
{% endblock %}
```

这个模板将在管理后台中显示一个简短的数据字段，可以根据需要进一步自定义。使用 `truncatechars` 模板过滤器可以限制显示的字符数。

选择适合你需求的方法，并根据需要进行自定义。

在 Django 模型类中定义一个方法来返回缩短后的数据是一个不错的主意，但直接在模型类中定义 `shortened_data()` 方法可能不是最佳方式。`shortened_data()` 方法的主要目的是为了在管理后台中更好地呈现数据，因此将这个方法放在 Admin 类中更合适。

你可以使用属性装饰器 (`@property`) 在模型类中创建一个属性，然后在 Admin 类中引用这个属性来显示缩短后的数据。下面是一个示例：

```
pythonCopy codefrom django.db import models

class HisInformation(models.Model):
    idcard = models.CharField(verbose_name='身份证号', max_length=18)
    year = models.IntegerField(verbose_name='年份', default=None)
    data = models.JSONField()

    class Meta:
        verbose_name = '就诊记录-历史记录'
        verbose_name_plural = verbose_name

    @property
    def shortened_data(self):
        data_str = str(self.data)
        return data_str[:50] + '...' if len(data_str) > 50 else data_str
```

然后在 Admin 类中使用 `shortened_data` 属性：

```
pythonCopy codefrom django.contrib import admin
from .models import HisInformation

@admin.register(HisInformation)
class HisInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'idcard', 'year', 'display_shortened_data',)

    def display_shortened_data(self, obj):
        return obj.shortened_data

    display_shortened_data.short_description = 'Shortened Data'
```

这样就能在 Admin 后台显示缩短的数据字段了。