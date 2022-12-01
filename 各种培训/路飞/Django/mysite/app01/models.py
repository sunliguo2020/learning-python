from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

    """
    create table app01_userinfo(
    id,bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int)
    
    CREATE TABLE `app01_userinfo` (
	`id` BIGINT ( 20 ) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR ( 32 ) COLLATE utf8mb4_bin NOT NULL,
	`password` VARCHAR ( 64 ) COLLATE utf8mb4_bin NOT NULL,
	`age` INT ( 11 ) NOT NULL,
PRIMARY KEY ( `id` ) 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_bin;
    
    python manage.py makemigrations
    python manage.py migrate
    """


class Department(models.Model):
    title = models.CharField(max_length=15)


class Role(models.Model):
    captionn = models.CharField(max_length=16)

# 新建数据

# UserInfo.objects.create(name='dsf',password='sdf',age=10)
