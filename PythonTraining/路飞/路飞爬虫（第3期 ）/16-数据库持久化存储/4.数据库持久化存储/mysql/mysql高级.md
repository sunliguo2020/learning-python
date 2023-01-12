### python操作链接数据库

- pymysql模块:pip install pymysql

  - 作用:可以实现使用python程序链接mysql数据库，且可以直接在python中执行sql语句

- ```sql
  import pymysql
  #1.创建链接对象
  conn = pymysql.Connect(
      host='127.0.0.1',#数据库服务器主机地址
      port=3306, #mysql的端口号
      user='root', #数据库的用户名
      password='boboadmin', #数据库密码
      db='AnHui',#数据仓库的名称
      charset='utf8')
  #创建一个游标对象
  cusor = conn.cursor()
  #2.增加记录操作
  # sql = 'insert into emp(name,sex,age,dep_id)values("%s","%s",%d,%d)'%('haha','female',20,200)
  # cusor.execute(sql)
  # conn.commit() #对数据进行整改后，记得进行事物的提交
  
  #3.删除记录
  # sql = 'delete from emp where name = "%s"'%'haha'
  # print(sql)
  # cusor.execute(sql)
  # conn.commit()
  
  #4.修改操作
  # new_age = input('enter a new age:')
  # new_age = int(new_age)
  # sql = 'update emp set age = %d where id = 3'%new_age
  # print(sql)
  # cusor.execute(sql)
  # conn.commit()
  
  #查询操作
  sql = 'select * from emp where age > 30'
  cusor.execute(sql) #负责执行sql语句
  #fetchall返回的是一个元组，元组元素又为一个元素，该元组中存储的是查询到的一条记录
  # all_data = cusor.fetchall() #获取查询到所有的数据，如果没有查询到数据返回一个空元组
  # print(all_data)
  
  #fetchone只会返回查询到的第一条数据
  one_data = cusor.fetchone() #如果没有查询到数据返回None
  print(one_data)
  
  #关闭打开的资源对象
  cusor.close()
  conn.close()
  
  ```


### 登录注册

```python
import pymysql
conn = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='boboadmin',
    db='AnHui',
    charset='utf8'
)
cusor = conn.cursor()

def regist():
    username = input('enter username:')
    password = input('enter password:')
    email = input('enter email:')
    phone = input('enter phone:')
    #判定用户名是否重复
    s = 'select * from userData where username="%s"'%username
    cusor.execute(s)
    r = cusor.fetchone()
    #如果查询到结果则表示用户名存在
    if r == None:
        sql = 'insert into userData(username,passwowrd,email,phone) values("%s","%s","%s","%s")'%(username,password,email,phone)
        cusor.execute(sql)
        conn.commit()
        print('注册成功！')
    else:
        print('注册失败，用户名已经存在！')
def login():
    username = input('enter username:')
    password = input('enter password:')
    sql1 = 'select * from userData where username="%s"'%username
    cusor.execute(sql1)
    r1 = cusor.fetchone()
    if r1 == None: #如果fetchone没有查询到数据返回的是None
        print('登录失败，用户名不存在！')
    else:#用户名存在
        pwd = r1[2]
        if pwd == password:
            print('登录成功！')
        else:
            print('登录失败，密码错误！')

```

### 事物处理(大致了解)

- 什么是事物？
  - Mysql的事物主要是指一组处理操作量大，复杂度高的数据的操作。
  - 事务其实就是MySQL中处理数据的一种方式,主要用在数据完整性高,数据之间依赖性大的情况下的一种数据处理方式.
  - 举个例子
  - ,在小张点击了确认转账的按钮时,系统突然崩溃了.会出现这样几中不正确的情况:
    - 1.小张的钱打到小李的账户上,但是自己的账户上的钱没被扣.
    - 2.小张的钱打没到小李的账户上了,但是自己账户上的钱被扣.
    - 这样的业务场景就需要MySQL事务保持,即使机器出故障的情况下,数据仍然是正确的.
  
- ```python
  import pymysql
  #1.创建链接对象
  conn = pymysql.Connect(
      host='127.0.0.1',#数据库服务器主机地址
      port=3306, #mysql的端口号
      user='root', #数据库的用户名
      password='boboadmin', #数据库密码
      db='AnHui',#数据仓库的名称
      charset='utf8')
  #创建一个游标对象
  cusor = conn.cursor()
  
  #小张向小李的银行卡打200块钱
  sql1 = 'update bankTab set monry -= 200 where name = "小张"'
  sql2 = 'update bankTab set monry += 200 where123 name = "小李"'
  
  try:
      cusor.execute(sql1) #成功执行
      cusor.execute(sql2) #发成异常
      conn.commit() #说明转账成功，数据就写死到数据库，没有办法在回撤
  except Exception as e:
      print(e)
      conn.rollback() #事物的回滚:将try中执行成功的sql效果撤回
      
  cusor.close()
  conn.close()
  ```
  
  
  
- 事物的特点
  
  - 原子性
    - 一个事务必须被作为一个不可分割的最小工作单元,每个事务中的所有操作必须要么成功,或者要么失败,永远不可能一些操作失败,一些操作成功,这就是所谓的原子性的概念.
  - 一致性
    - 一致性就像上面举的一个例子一样,当发生异常情况下,数据仍然是正确的.就是说当一个事务执行失败了,数据之间是不会受异常的情况而影响,永远保持着他的正确性.
  - 隔离性
    - 当一个事务还未提交,每个事务之间是相互隔离的,互补受到影响.
  - 持久性
    - 当一个事务进行提交之后,发生的变化就会永远保存在数据库中.
  
- 事物的提交和回滚
  - commit
  - rollback

