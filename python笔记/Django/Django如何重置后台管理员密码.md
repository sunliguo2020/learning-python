
打开终端后，连续输入以下代码, 先根据管理员用户名获取对象，然后使用set_password方法重置密码，最后保存。
```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(username='your username')
>>> user.set_password('your new password')
>>> user.save()
>>> quit()

```



如果你连管理员用户名都忘了，你要根据id获取用户对象，一般默认第一个用户一般是superuser(超级用户)。
```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.get(pk=1)
>>> user
< User:  username>
>>> user.set_password('your new password')
>>> user.save()
>>> quit()

```

