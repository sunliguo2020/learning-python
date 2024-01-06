开发中有时需要删除已有的数据库表并重新建表，这在Django开发中需要做些额外的工，因为Django会对Model到表的创建修改情况做保存。



正确的方法如下：

1.先到数据库把表删掉：drop table

2.注释Django中对应的Model

3.执行以下命令：



```python
python manage.py makemigrations
python manage.py migrate --fake
```


4.去掉步骤2中的注释



```python
python manage.py makemigrations
python manage.py migrate
```