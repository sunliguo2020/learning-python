from urllib import request

from django import forms
from django.core.files.base import ContentFile
from slugify import slugify

from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("The given Url does not match valid image extension.")
        return url

    # 将表单提交的数据保存到数据库。
    # 实现实例对象的保存。
    def save(self, force_insert=False, force_update=False, commit=True):
        # ImageForm的实例对象，没有保存
        # Save this form's self.instance object if commit=True.

        image_model_object = super(ImageForm, self).save(commit=False)  # 返回一个模型对象
        # print(f"第一个image的类型:{type(image)}")
        # print(f"dir(image):{dir(image)}")
        # print(image.image)  # <class 'django.db.models.fields.files.ImageFieldFile'>
        # print(dir(image.image))
        # print(image.image.name)
        image_url = self.cleaned_data['url']
        image_name = f"{slugify(image_model_object.title)}.{image_url.rsplit('.', 1)[1].lower()}"
        # print(f"{image_name}")
        response = request.urlopen(image_url)

        # 第一个image  ImageForm实例对象
        # 第二个image Image模型类的image字段
        # class Storage .save()
        # 保存文件到文件系统中
        # image.image = 'images/2023/09/16/xin-de-ce-shi.jpg'
        image_model_object.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image_model_object.save()
        return image_model_object
