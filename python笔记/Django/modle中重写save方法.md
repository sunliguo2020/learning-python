如果您想在 Django 模型中重写 `save` 方法，以便从 URL 中获取图片并保存到模型中，可以像下面这样操作： 

```python
import requests
from django.db import models
from django.core.files.base import ContentFile

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_file = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        # 如果模型没有保存过或者没有指定图片文件
        if not self.pk and self.image_file:
            try:
                response = requests.get(self.image_file)  # 获取图片 URL 中的内容
                if response.status_code == 200:
                    # 使用 ContentFile 将图片内容作为文件对象保存到 image_file 字段中
                    self.image_file.save(f'{self.title}.jpg', ContentFile(response.content), save=False)
            except Exception as e:
                pass  # 可以添加错误处理逻辑

        super(Image, self).save(*args, **kwargs)  # 调用父类的 save 方法保存模型

```

在这个示例中，我们重写了 `save` 方法，在模型对象保存之前会检查是否已经指定了图片的 URL (`self.image_file`)。如果存在 URL，它将尝试使用 `requests` 库获取图片内容，并使用 `ContentFile` 将其作为文件对象保存到 `image_file` 字段中。然后调用父类的 `save` 方法保存模型。

请注意，这只是一个简单的示例。在实际应用中，您可能需要添加更多的错误处理和验证逻辑，以确保 URL 的有效性、图片的下载和保存过程的稳定性。