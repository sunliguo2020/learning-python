#  1，继承AbstractUser 

models.py

```python
from django.contrib.auth.models import AbstractUser
class UserData(AbstractUser):
    desc=models.TextField()
    class Meta:
        db_table = 'userData'

```



admin.py

```python
from blog.models import UserData
admin.site.register(UserData)
```

setting.py(添加)

```python
AUTH_USER_MODEL='blog.UserData'
```


同步数据库，最好修改数据库名称，以防出现问题。(test.sqlite3)

```python
cd /d ...
manage.py makemigrations blog
manage.py migrate
```

#  2,profile扩展 

models.py

```python
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    desc=models.TextField(blank=True,null=True)
    class Meta:
        db_table = 'profile'
```



admin.py

```python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import UserProfile

class ProfileInLine(admin.StackedInline):
    model=UserProfile
    verbose_name="profile"
    
class UserAdmin(admin.ModelAdmin):
    inlines=(ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

```



setting.py(去除)

#AUTH_USER_MODEL='blog.UserData'
1
同步数据库，最好修改数据库名称，以防出现问题。

cd /d ...
manage.py makemigrations blog
manage.py migrate
