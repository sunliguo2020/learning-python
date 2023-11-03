### 初始化项目

1、创建虚拟环境

```
python -m venv venv
```

2、激活虚拟环境

```
venv\Scfripts\acitvate
```

3、安装django及pillow

```
pip instal Django pillow
```

4、创建baykeproject目录

```
django-admin startproject baykeproject .
```

5、创建baykeshop目录

6、创建common目录

7、创建conf目录

8、同步数据库

```
python manage.py makemigrations
python manage.py migrate

```

9、运行项目

```
python manage.py runserver
```



### 开发流程

1、创建app

在apps 目录中新建article目录

django-admin startapp app名  app路径

```

(venv) D:\github\learning-python\Django\bayke-shop>django-admin startapp article baykeshop\apps\article
CommandError: Destination directory 'D:\github\learning-python\Django\bayke-shop\baykeshop\apps\article' does not exist, please create it first.

(venv) D:\github\learning-python\Django\bayke-shop>django-admin startapp article bakeshop\apps\article  
```



2、settings中注册app

修改app类名

```
class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakeshop.apps.article'

```

注册

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bakeshop.apps.article'
]
```



3、编写视图views

函数视图 类试图

4、urls.py中注册视图路由

5、项目路由urls.py中引入app urls路由

6、创建模型

7、迁移同步数据库

8、视图中查询数据动态交互