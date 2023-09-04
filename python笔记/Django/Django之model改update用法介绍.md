### model改update常规用法

假如我们的表结构是这样的

```python
class User(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')
```


那么我们修改用户名和状态可以使用如下两种方法：

##### 方法一：

```python
User.objects.filter(id=1).update(username='nick',is_active=True)
```

##### 方法二：

```python
_t = User.objects.get(id=1)
_t.username='nick'
_t.is_active=True
_t.save()
```



方法一适合更新一批数据，类似于mysql语句update user set username='nick' where id = 1

方法二适合更新一条数据，也只能更新一条数据，当只有一条数据更新时推荐使用此方法，另外此方法还有一个好处，我们接着往下看

具有auto_now属性字段的更新
我们通常会给表添加三个默认字段 - 自增ID，这个django已经默认加了，就像上边的建表语句，虽然只写了username和is_active两个字段，但表建好后也会有一个默认的自增id字段 

- 创建时间，用来标识这条记录的创建时间，具有auto_now_add属性，创建记录时会自动填充当前时间到此字段 
-  修改时间，用来标识这条记录最后一次的修改时间，具有auto_now属性，当记录发生变化时填充当前时间到此字段。

就像下边这样的表结构



```python
class User(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')
```



当表有字段具有auto_now属性且你希望他能自动更新时，必须使用上边方法二的更新，不然auto_now字段不会更新，也就是：

_t = User.objects.get(id=1)
_t.username='nick'
_t.is_active=True
_t.save()

#### json/dict类型数据更新字段

目前主流的web开放方式都讲究前后端分离，分离之后前后端交互的数据格式大都用通用的json型，那么如何用最少的代码方便的更新json格式数据到数据库呢？同样可以使用如下两种方法：

方法一：

data = {'username':'nick','is_active':'0'}
User.objects.filter(id=1).update(**data)
同样这种方法不能自动更新具有auto_now属性字段的值
通常我们再变量前加一个星号(*)表示这个变量是元组/列表，加两个星号表示这个参数是字典
方法二：

```python

data = {'username':'nick','is_active':'0'}
_t = User.objects.get(id=1)
_t.__dict__.update(**data)
_t.save()
```



方法二和方法一同样无法自动更新auto_now字段的值
注意这里使用到了一个__dict__方法
方法三：

```python
_t = User.objects.get(id=1)
_t.role=Role.objects.get(id=3)
_t.save()
```





ForeignKey字段更新
假如我们的表中有Foreignkey外键时，该如何更新呢？

class User(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, verbose_name='角色')
方法一：

User.objects.filter(id=1).update(role=2)
最简单的方法，直接让给role字段设置为一个id即可
当然也可以用dict作为参数更新：
User.objects.filter(id=1).update(**{'username':'nick','role':3})
方法二：

_role = Role.objects.get(id=2)
User.objects.filter(id=1).update(role=_role)
也可以赋值一个实例给role
当然也可以用dict作为参数更新：
_role = Role.objects.get(id=1)
User.objects.filter(id=1).update(**{'username':'nick','role':_role})
方法三：

_t = User.objects.get(id=1)
_t.role=Role.objects.get(id=3)
_t.save()
注意：这里的role必须赋值为一个对象，不能写id，不然会报错"User.role" must be a "Role" instance
当使用dict作为参数更新时又有一点不同，如下代码：
_t = User.objects.get(id=1)
_t.__dict__.update(**{'username':'nick','role_id':2})
_t.save()
Foreignkey外键必须加上_id，例如：{'role_id':3}
role_id后边必须跟一个id（int或str类型都可），不能跟role实例
ManyToManyField字段更新
假如我们的表中有ManyToManyField字段时更新又有什么影响呢？

class User(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, verbose_name='角色')
    groups = models.ManyToManyField(Group, null=True, verbose_name='组')
m2m更新：m2m字段没有直接更新的方法，只能通过清空再添加的方法更新了

_t = User.objects.get(id=1)
_t.groups.clear()
_t.groups.add(*[1,3,5])
_t.save()
add()：m2m字段添加一个值，当有多个值的时候可用列表，参照上边例子
_t.groups.add(2)
_t.groups.add(Group.objects.get(id=2))
remove()：m2m字段移除一个值，，当有多个值的时候可用列表，参照上边例子
_t.groups.remove(2)
_t.groups.remove(Group.objects.get(id=2))
clear()：清空m2m字段的值
