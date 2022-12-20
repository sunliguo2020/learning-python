要使用static标签，首先需要

```python
{% load static %}
```

加载静态文件步骤

1、

```python
INSTALLED_APPS = [
   
    'django.contrib.staticfiles',
   
]
```

2、

```python
STATIC_URL = 'static/'
```



3、

在已经安装了的app下创建一个文件夹叫做static，然后再在这个static文件夹下创建一个当前app的名字的文件夹，再把静态文件放到这个文件夹下。例如你的app叫做book，有一个静态文件叫做book.jpg，那么路径为book/static/book/book.jpg。（为什么在app下创建一个static文件夹，还需要在这个static下创建一个同app名字的文件夹呢？原因是如果直接把静态文件放在static文件夹下，那么在模版加载静态文件的时候就是使用book.jpg，如果在多个app之间有同名的静态文件，这时候可能就会产生混淆。而在static文件夹下加了一个同名app文件夹，在模版中加载的时候就是使用app名/book.jpg，这样就可以避免产生混淆。）
注意： 文件夹的名字必须为static 。
如果有一些静态文件是不和任何app挂钩的。即不再任何一个app的目录下。那么可以在settings.py中添加STATICFILES_DIRS，以后DTL就会在这个列表的路径中查找静态文件。例如我们在manage.py的同级目录下新建一个static的文件夹。然后在settings.py:中添加STATICFILES_DIRS
STATICFILES_DIRS = [
	os.path.join(BASE_DIR,"static")
]
1
2
3
注： 第三种和第四种方法都可以加载静态文件，我的个人习惯是在manage.py的同级目录下新建一个static文件夹，然后将所有的静态文件进行分类的在里面存储。而不去app中新建一个static的文件夹。但这只是我的个人习惯。毕竟不管是黑猫白猫，能抓到老鼠的就是好猫，所以只要我们能把项目做出来能运行，并且代码结构有逻辑性、层次感就行了。
