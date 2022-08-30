### redis基本使用

- 介绍：
  - redis是一款非关系型数据库或者缓存数据库（性能最高的非关系型数据库之一），拥有每秒近十万次的读写能力。

- 安装&启动

  - 安装：

    - 使用免安装版本即可，免安装版本压缩包在window和mac文件夹中，对压缩包解压缩即可。

  - 启动：

    - window：

      - 终端进入到解压缩文件夹的bin目录下，执行./redis-server启动服务，执行./redis-cli启动客户端

    - mac：

      - 终端进入到解压缩文件夹的src目录下，执行./redis-server启动服务，执行./redis-cli启动客户端

    - ```python
      redis-cli #无密码且数据库在你本机，执行该指令
      redis-cli -h ip地址 -p 端口 --raw  auth 密码   
      #raw可以让redis显示出中文(windows无效)如果有密码可以这样来登录, 如果没有,不用这一步
      ```

- redis常见数据类型

  - string类型

    - ```
      set key value  # 添加一条数据
      get key		   # 查看一条数据
      ```

  - hash类型

    - ```
      hset key k1 v1   # 将k1, v1存储在key上
      hget key k1      # 将key上的k1提取出来
      hmset key k1 v1 k2 v2 k3 v3....  # 一次性将多个k,v存储在key
      hmget key k1 k2....# 一次性将key中的k1, k2...提取出来
      hgetall key 	# 一次性将key中所有内容全部提取
      hkeys key		# 将key中所有的k全部提取
      hvals key 		# 将key中所有的v全部提取
      
      例如：
      hmset stu id 1 name bobo age 18
      HMGET stu name age   # bobo 18
      ```

  - list类型(重点)：底层是一个双向链表. 可以从左边和右边进行插入

    - ```
      LPUSH key 数据1 数据2 数据3.... # 从左边插入数据
      RPUSH key 数据1 数据2 数据3.... # 从右边插入数据
      LRANGE key start stop     # 从start到stop提取数据. 
      
      LLEN key	# 返回key对应列表的长度
      LPOP key  # 从左边删除一个.并返回被删除元素
      RPOP key	# 从右边删除一个.并返回被删除元素
      ```

  - set类型（重点）：set是无序的超大集合。无序, 不重复

    - ```
      SADD key 值   # 向集合内存入数据
      SMEMBERS key  # 查看集合内所有元素
      SPOP key  # 随机从key中删除一个数据
      ```

### python链接redis

- 环境安装：pip install redis==2.10.6

- ```python
  import redis
  #创建链接对象
  conn = redis.Redis(host='127.0.0.1',port=6379)
  #插入数据
  # result = conn.sadd('class','num4')
  # print(result)
  
  # result = conn.lpush('hobby','haha')
  # print(result)
  
  #查询set集合里的数据
  print(conn.smembers('class'))
  ```

