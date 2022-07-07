python mysql

ddl操作数据库

创建数据库

```sql
create databases 数据库名;
create databases if  not exists 数据库名;
create databases 数据库名  character set 字符集;
CREATE DATABASE `guotu` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin';

```

<<<<<<< HEAD
#### 查看数据库
=======
查看数据库
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```sql

show databases;
shw create database 数据库名;

```

<<<<<<< HEAD
#### 修改数据库
=======
修改数据库
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```sql
alter database 数据库名 default character set 字符集;
```

<<<<<<< HEAD
#### 删除数据库
=======
删除数据库
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```sql
drop database 数据库名
```

<<<<<<< HEAD
#### 使用数据库
=======
使用数据库
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```sql
select database();
use 数据库名;
```

<<<<<<< HEAD
#### DDL操作表
=======
DDL操作表
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

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

<<<<<<< HEAD
#### 查看表
=======
查看表
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

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
#### 删除表
=======
删除表
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```sql
---直接删除表名
drop table 表名;
---判断表是否存在并删除
drop table if exists 表名;
```

<<<<<<< HEAD
#### DML语句
=======
DML语句
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

增 

```sql
insert into users values('leanna',2111,2);

insert into shoujihao (PROD_INST_ID,CUST_ID,LATN,BUSI_NBR,USER_NAME,CUST_NAME,INSTALL_ADDR,CERTIFICATES_NBR,mod_time) select * from ziliao_old.phone limit 1;
```

删

```sql
delete from users where projid = %d;
delete from shoujihao where `mod_time` = '';
```

改

```sql
	update users set projid = 4 where projid = 2;

​	update  shoujihao  set `INSTALL_ADDR` = '' where `INSTALL_ADDR` is NULL limit 100000;

​	update shoujihao set `DUSI_ID` =''  ,INSTLL_ADDR='' where xxx;
 UPDATE 表名 SET 字段名=replace(字段名, ‘被替换字符串’, '用来替换的字符串') ;
 mysql> UPDATE kuandai SET `INSTALL_ADDR`=replace(INSTALL_ADDR, "'", '') ;
Query OK, 65 rows affected (6.90 sec)
Rows matched: 750210  Changed: 65  Warnings: 0
```

查

```sql
SELECT * FROM `shoujihao` WHERE `BUSI_NBR` LIKE '%13001500044%' ORDER BY `BUSI_NBR` LIMIT 0, 1000
SELECT * FROM `crawl`.`guhua` WHERE `file_name` LIKE '%5406399%' ORDER BY `id` DESC LIMIT 0,1000
SELECT * FROM `shoujihao` WHERE `CUST_ID` IS NULL LIMIT 0, 1000
SELECT * FROM `ziliao`.`shoujihao` WHERE `id` = '36' AND `BUSI_NBR` LIKE '%156%' ORDER BY `INSTALL_ADDR` LIMIT 0,1000;
不等于：
		<>

```

<<<<<<< HEAD
#### limit的使用
=======
limit的使用
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

####limit关键字可以接受1个或者两个参数，且这个参数需是整数常量。如果是两个参数，第一个表示返回记录行的偏移量，第二个表示返回记录行的最大数目。一个数的话，默认初识记录为0.

```sql
select * from table limit [offset,]rows | rows ;
```



例子：

查询某列唯一值

```sql

select distinct 列名 from   表名;
```



#### mysql 中null 和空值的区别

1.概念上 不同

- 空值不占空间

- null值占空间

空值表示一个杯子是真空状态，什么都没有。而NULL值是杯子中有空气。

定义为NOT NULL的字段只能插入空值，不能插入NULL值，而NULL值可以插入空值，也可以插入NULL值。



判断NULL值只能用is null 或is not null 不能用 = 或者<>



<<<<<<< HEAD
#### pymysql
=======
pymysql
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172

```python
db = pymysql.connect(host ='localhost',
                    user='root',
                    password='123456',
                    database='userinfo',
                    charset = 'utf-8')
cur = db.cursor()
sql = "insert into userinfo (username,password) values ('vera','1234')"
cur.execute(sql)
```

```sql
cur.fetchone()

返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None

cur.fetchall() 

返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()

需要注明：在MySQL中是NULL，而在Python中则是None
```

<<<<<<< HEAD
```
result = cur.fetchone()
        while result:
            yield result
            result = cur.fetchone()

```

=======
>>>>>>> 9033d61e7ecebbe38dfa95274e33c88795190172
