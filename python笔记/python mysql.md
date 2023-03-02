# python mysql

ddl操作数据库

创建数据库

```sql
create databases 数据库名;
create databases if  not exists 数据库名;
create databases 数据库名  character set 字符集;
CREATE DATABASE `guotu` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin';

```

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
<<<<<<< HEAD
<<<<<<< HEAD

=======
<<<<<<< HEAD
查看数据库
=======
>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00


>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
#### 查看数据库
```sql

show databases;
show create database 数据库名;

```

<<<<<<< HEAD
#### 修改数据库
=======
<<<<<<< HEAD
#### 修改数据库
=======

<<<<<<< HEAD
#### 修改数据库
=======
=======

#### 修改数据库
<<<<<<< HEAD
>>>>>>> 
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
=======

>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00

>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
```sql
alter database 数据库名 default character set 字符集;
```


<<<<<<< HEAD

#### 删除数据库

=======
<<<<<<< HEAD

#### 删除数据库

=======
<<<<<<< HEAD
#### 删除数据库
=======
<<<<<<< HEAD

=======

#### 删除数据库
>>>>>>> 
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
=======

#### 删除数据库
>
>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

```sql
drop database 数据库名
```


<<<<<<< HEAD

#### 使用数据库

=======
<<<<<<< HEAD

#### 使用数据库

=======
<<<<<<< HEAD
#### 使用数据库

=======
<<<<<<< HEAD

=======
=======
>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00

#### 使用数据库
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

```sql
select database();
use 数据库名;
```

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======


#### DDL操作表
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc

>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
#### DDL操作表
创建表

```sql
create table 表名（
字段名 字段类型 约束，
字段名 字段类型 约束）;
----快速创建一个表结构相同的表
create table 新表名 like 旧表名;
```

```sql
CREATE TABLE `guhua` (
	`id` INT ( 11 ) NOT NULL AUTO_INCREMENT,
	`file_name` CHAR ( 50 ) NOT NULL,
	`md5sum` CHAR ( 32 ) NOT NULL,
	`blob` MEDIUMBLOB NOT NULL,
	`mod_time` datetime NOT NULL,
	PRIMARY KEY ( `id` ),
	KEY `md` ( `md5sum` ) USING HASH,
KEY `fn` ( `file_name` ) USING HASH 
) ENGINE = MyISAM AUTO_INCREMENT = 6076474 DEFAULT CHARSET = utf8mb4;
```


#### 查看表

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======

>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

```sql
show tables;
---查看表结构
desc 表名;
---查看创建表的sql语句
show create table 表名;

```

修改表结构

```sql
---添加表列
alter table 表名 add 列名 类型;
---修改列类型
alter table 表名 modify 列名 新类型;
---修改列名
alter table 表名 change 旧列名 新列名 类型;
---删除列
alter table 表名 drop 列名;
---修改表名
rename table 表名 to 新表名;
---修改字符集
alter table 表名 character set 字符集;
添加自增字段，主键
ALTER TABLE `ziliao`.`kuandai` 
ADD COLUMN `id` int NOT NULL AUTO_INCREMENT FIRST,
ADD PRIMARY KEY (`id`);

ALTER TABLE `guotu`.`ip_arp` 
ADD COLUMN `id` int NOT NULL AUTO_INCREMENT FIRST,
ADD PRIMARY KEY (`id`);

```

<<<<<<< HEAD


=======
<<<<<<< HEAD


=======
<<<<<<< HEAD
=======



#### 删除表

>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc

>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
#### 删除表
```sql
---直接删除表名
drop table 表名;
---判断表是否存在并删除
drop table if exists 表名;
```


#### DML语句

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
<<<<<<< HEAD
=======

>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

增 

```sql
insert into users values('leanna',2111,2);
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
insert into shoujihao (PROD_INST_ID,CUST_ID,LATN,BUSI_NBR,USER_NAME,CUST_NAME,INSTALL_ADDR,CERTIFICATES_NBR,mod_time) select * from ziliao_old.phone limit 1;
```

删

```sql
delete from users where projid = %d;
delete from shoujihao where `mod_time` = '';
<<<<<<< HEAD
delete from PersonalId where personid is NULL;
=======
<<<<<<< HEAD
delete from PersonalId where personid is NULL;
=======
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
```

改

```sql
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
update users set projid = 4 where projid = 2;
update  shoujihao  set `INSTALL_ADDR` = '' where `INSTALL_ADDR` is NULL limit 100000;
update shoujihao set `DUSI_ID` =''  ,INSTLL_ADDR='' where xxx;
UPDATE 表名 SET 字段名=replace(字段名, ‘被替换字符串’, '用来替换的字符串') ;
UPDATE kuandai SET `INSTALL_ADDR`=replace(INSTALL_ADDR, "'", '') ;

<<<<<<< HEAD
=======
=======
	update users set projid = 4 where projid = 2;

​	update  shoujihao  set `INSTALL_ADDR` = '' where `INSTALL_ADDR` is NULL limit 100000;

​	update shoujihao set `DUSI_ID` =''  ,INSTLL_ADDR='' where xxx;
 UPDATE 表名 SET 字段名=replace(字段名, ‘被替换字符串’, '用来替换的字符串') ;
 mysql> UPDATE kuandai SET `INSTALL_ADDR`=replace(INSTALL_ADDR, "'", '') ;
Query OK, 65 rows affected (6.90 sec)
Rows matched: 750210  Changed: 65  Warnings: 0
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
```

查

```sql
SELECT * FROM `shoujihao` WHERE `BUSI_NBR` LIKE '%13001500044%' ORDER BY `BUSI_NBR` LIMIT 0, 1000
SELECT * FROM `crawl`.`guhua` WHERE `file_name` LIKE '%5406399%' ORDER BY `id` DESC LIMIT 0,1000
SELECT * FROM `shoujihao` WHERE `CUST_ID` IS NULL LIMIT 0, 1000
SELECT * FROM `ziliao`.`shoujihao` WHERE `id` = '36' AND `BUSI_NBR` LIKE '%156%' ORDER BY `INSTALL_ADDR` LIMIT 0,1000;
<<<<<<< HEAD
不等于：
		<>

```


#### limit的使用


limit关键字可以接受1个或者两个参数，且这个参数需是整数常量。如果是两个参数，第一个表示返回记录行的偏移量，第二个表示返回记录行的最大数目。一个数的话，默认初识记录为0.

不等于：<>

```sql
select * from table limit [offset,]rows | rows ;
```




例子：



#### 查询某列唯一值


```sql

select distinct 列名 from   表名;
```



#### mysql 中null 和空值的区别

1.概念上 不同

- 空值不占空间

- null值占空间

空值表示一个杯子是真空状态，什么都没有。而NULL值是杯子中有空气。

定义为NOT NULL的字段只能插入空值，不能插入NULL值，而NULL值可以插入空值，也可以插入NULL值。

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

判断NULL值只能用is null 或is not null 不能用 = 或者<>

```sql
select count(*) from PersonalId where personid is NULL;
select count(*) from PersonalId where personid is not NULL;
```




#### pymysql

<<<<<<< HEAD
=======
=======
<<<<<<< HEAD


判断NULL值只能用is null 或is not null 不能用 = 或者<>

#### pymysql


<<<<<<< HEAD


#### pymysql
=======
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

```python
db = pymysql.connect(host ='localhost',
                    user='root',
                    password='123456',
                    database='userinfo',
                    charset = 'utf-8')
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
#创建游标对象
cur = db.cursor()
sql = "insert into userinfo (username,password) values ('vera','1234')"
#使用execute()方法执行sql查询
<<<<<<< HEAD
=======
=======
cur = db.cursor()
sql = "insert into userinfo (username,password) values ('vera','1234')"
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
cur.execute(sql)
```

```sql
cur.fetchone()
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None

cur.fetchall() 

返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()

需要注明：在MySQL中是NULL，而在Python中则是None
```

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
```py
 #执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
 execute(self, query, args):
#执行单条sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
　executemany(self, query, args):
```



```python

<<<<<<< HEAD
=======
=======

<<<<<<< HEAD
```
=======

```python
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
result = cur.fetchone()
        while result:
            yield result
            result = cur.fetchone()

```
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f

##### 在使用pymysql的executemany方法时，需要注意的几个问题

1、在写sql语句时，不管字段为什么类型，占位符统一使用%s,且不能加上引号。例如

```python
sql="insert into tablename (id,name) values (%s,%s)"
```

2、添加的数据的格式必须为list[tuple(),tuple(),tuple()]或者tuple(tuple(),tuple(),tuple())例如

```python
values=[(1,"zhangsan"),(2,"lisi")]
#或者
values=((1,"zhangsan"),(2,"lisi"))
```

最后，通过executemany插入

```python
cursor.executemany(sql,values) 
```



<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======

<<<<<<< HEAD
>>>>>>> 4d0ede0c3f44f1883275844924f649f10fe155bc
=======
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
重复字段：

查询user表中，user_name字段值重复的数据及重复次数

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
```sql
select user_name,count(*) as count from user group by user_name having count>1;
```

<<<<<<< HEAD
=======
=======
```
select user_name,count(*) as count from user group by user_name having count>1;
```
>>>>>>> 44cd2abc499f1b697db5f17c13be08680ed0ce00
>>>>>>> 916441d61397f5ac1f8eb6cb97f9b7ebf1e5cdb7
>>>>>>> 9fea01ce2b50beffd7fb016f8b33d6f7166ad34f
