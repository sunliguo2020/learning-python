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

2、settings中注册app

3、编写视图views

4、urls.py中注册视图路由

5、项目路由urls.py中引入app urls路由

6、创建模型

7、迁移同步数据库

8、视图中查询数据动态交互