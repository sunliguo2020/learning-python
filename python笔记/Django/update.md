model update常规用法

表结构

```python
class User(models.Model):
    username = models.CharField(max_length=255,unique=True,verbose_name='用户名')
    is_active= models.BooleanField(default=False,verbose_name='激活状态')
```

修改用户名和状态可以使用如下两种方法：

方法一：

```python
User.object.filter(id=1).update(username='nick',is_active=True)
```

方法二：

```python
_t = User.objects.get(id=1)
_t.username='nick'
_t.is_active = True
_t.save()
```

方法一适合更新一批数据，类似于mysql语句 update user set username='nick' where id=1

方法二适合更新一条数据，也只能更更新一条数据，此方法还有另外一个好处

#### 具有auto_now属性字段的更新

我们通常会给表添加三个默认字段

- 自增ID，Django默认添加自增id字段

- 创建时间，用来标记这条记录的创建时间，具有auto_now_add属性，创建记录自动填充当前时间

- 修改时间，标识这条记录最后一次的修改时间，具有auto_now属性，当记录发生变化时填充当前时间

  ```python
  class User(models.Model):
      create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
      update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
      username = models.CharField(max_length=255,unique=True,verbose_name='用户名')
      is_active= models.BooleanField(default=False,verbose_name='激活状态')
  	
  ```

  当表有字段具有auto_now属性且你希望他能自动更新时，必须使用上面方法二更新。

  ```python
  _t = User.objects.get(id=1)
  _t.username = 'nick'
  _t.is_active=  True
  _t.save()
  ```

  #### json/dict类型数据更新字段

  方法一：

  ```python
  data = {'username':'nick','is_active':'0'}
  user.objects.filter(id=1).update(**data)
  ```

  - 同样这种方法不能自动更新具有auto_now属性字段的值

  - 通常我们在变量前加一个星号（*）表示这个变量时元组/列表，加两个型号表示这个参数时字典

    方法二、

    ```ptyhon
    data = {'username':'nick','is_activ':'0'}
    _t = User.object.get(id=1)
    _t.__dict__.update(**data)
    _t.save()
    ```

    - 方法二和方法一同样无法自动更新auto_now字段的值

    - 这里使用了一个__dict__   方法

      方法三、

      ```python
      
      _t = User.objects.get(id=1)
      _t.role = Role.object.get(id=3)
      _t.save()
      ```

      