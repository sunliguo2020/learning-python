ImageField 保存图像文件的字段。

使用步骤：

##### 1、配置settings.py

```python
# settings.py

# 配置 MEDIA_ROOT 作为你上传文件在服务器中的基本路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') # 注意此处不要写成列表或元组的形式
# 配置 MEDIA_URL 作为公用 URL，指向上传文件的基本路径
MEDIA_URL = '/media/'
# 这里特意写成 upload 和 media，而不是统一写成 media 或 upload，是为了便于理解 MEDIA_ROOT 和 MEDIA_URL 的作用和区别
```

##### 2、models.py 中设置ImageField字段

example:

```python
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to="uploads/")
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to="uploads/%Y/%m/%d/")
```

example 2:

```python
For example:

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
```



```python

"""
处理上传的图片文件的路径
upload_to may also be a callable, such as a function. This will be called to obtain the upload path, including the filename. This callable must accept two arguments and return a Unix-stylepath (with forward slashes) to be passed along to the storage system. The two arguments are:

Argument	Description
instance	An instance of the model where the ImageField is defined. More specifically, 
            this is a particular instance where the current file is being attached.
filename	The filename that was originally given to the file. This may or may not be taken   into account when determining the final destination path
"""
```



```python
# models.py

def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename) # 系统路径分隔符差异，增强代码重用性

class Student(models.Model):
    major = models.ForeignKey(Major, on_delete = models.CASCADE)
    name = models.CharField('姓名', max_length = 10)
    identity_card = models.CharField('身份证号', max_length = 20, unique = True)
    ......    
    # upload_to 参数接收一个回调函数 user_directory_path，该函数返回具体的路径字符串，图片会自动上传到指定路径下，即 MEDIA_ROOT + upload_to
    # user_directory_path 函数必须接收 instace 和 filename 两个参数。参数 instace 代表一个定义了 ImageField 的模型的实例，说白了就是当前数据记录；filename 是原本的文件名
    # null 是针对数据库而言，如果 null = True, 表示数据库的该字段可以为空；blank 是针对表单的，如果 blank = True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    photo = models.ImageField('照片', upload_to = user_directory_path, blank = True, null = True)
    ......
    # 这里定义一个方法，作用是当用户注册时没有上传照片，模板中调用 [ModelName].[ImageFieldName].url 时赋予一个默认路径    
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/media/default/user.jpg'
```

