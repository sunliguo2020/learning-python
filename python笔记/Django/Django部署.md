#### 1、创建虚拟环境

python自带的轻量级虚拟环境venv

```python
root@3865u:~# python3 -m venv venv
```

激活和退出虚拟环境

```PYTHON
root@3865u:~# source venv/bin/activate
(venv) root@3865u:~# deactivate
root@3865u:~#

```

#### 2、安装Django

```python
(venv) root@3865u:~# pip list
Package       Version
------------- -------
pip           20.3.4
pkg-resources 0.0.0
setuptools    44.1.1
(venv) root@3865u:~# pip install django
Collecting django
  Downloading Django-4.1.5-py3-none-any.whl (8.1 MB)
     |████████████████████████████████| 8.1 MB 27 kB/s
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.3-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 34 kB/s
Collecting asgiref<4,>=3.5.2
  Downloading asgiref-3.6.0-py3-none-any.whl (23 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.6.0 django-4.1.5 sqlparse-0.4.3

```

#### 3、安装uwsgi软件

1、安装uwsgi软件

```python
(venv) root@3865u:~/venv/bin# pip install uwsgi
Collecting uwsgi
  Downloading uwsgi-2.0.21.tar.gz (808 kB)
     |████████████████████████████████| 808 kB 80 kB/s
Using legacy 'setup.py install' for uwsgi, since package 'wheel' is not installed.
Installing collected packages: uwsgi
    Running setup.py install for uwsgi ... done
Successfully installed uwsgi-2.0.21

```

2、查看版本

```python
(venv) root@3865u:~/venv/bin# uwsgi --version
2.0.21
(venv) root@3865u:~/venv/bin# uwsgi --python-version
3.9.2

```

#### 4、启动并测试uwsgi

1、编写一个测试uwsgi的简单python脚本

```python
(venv) root@3865u:~/venv# cat test_uwsgi.py
def application(env,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b"Hello Django"]

```

2、启动uwsgi，在端口9000上开放web访问。

```python
(venv) root@3865u:~/venv# uwsgi --http :9000 --wsgi-file test_uwsgi.py
*** Starting uWSGI 2.0.21 (64bit) on [Wed Feb  8 13:14:24 2023] ***
compiled with version: 10.2.1 20210110 on 08 February 2023 05:07:18
os: Linux-5.10.0-10-amd64 #1 SMP Debian 5.10.84-1 (2021-12-08)
nodename: 3865u
machine: x86_64
clock source: unix
detected number of CPU cores: 2
current working directory: /root/venv
detected binary path: /root/venv/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** WARNING: you are running uWSGI without its master process manager ***
your processes number limit is 11811
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI http bound on :9000 fd 4
spawned uWSGI http 1 (pid: 2446292)
uwsgi socket 0 bound to TCP address 127.0.0.1:38695 (port auto-assigned) fd 3
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
Python version: 3.9.2 (default, Feb 28 2021, 17:03:44)  [GCC 10.2.1 20210110]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x55da42b83790
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 72904 bytes (71 KB) for 1 cores
*** Operational MODE: single process ***
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x55da42b83790 pid: 2446291 (default app)
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) ***
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI worker 1 (and the only) (pid: 2446291, cores: 1)

```

#### 5、uwsgi 配置文件

```python
[root@aliyun ITAM]# more uwsgi.ini
#添加配置选择
[uwsgi]
#配置和nginx连接的socket连接
socket=127.0.0.1:8997
#http= 0.0.0.0:8996
#配置项目路径，项目的所在目录
chdir=/root/ITAM/
#配置wsgi接口模块文件路径,也就是wsgi.py这个文件所在的目录名
wsgi-file=/root/ITAM/ITAM/wsgi.py
#虚拟环境目录
home=/root/dj-env
#配置启动的进程数
processes=4
#配置每个进程的线程数
threads=2
#配置启动管理主进程
master=True
#配置存放主进程的进程号文件
pidfile=uwsgi.pid
#配置dump日志记录
daemonize=uwsgi.log
uid=990

```

#### 6、uwsgi常用命令

```python
启动：uwsgi --ini  uwsgi.ini
重启： uwsgi --reload uwsgi.pid
停止： uwsgi --stop uwsgi.pid
```

启停脚本：

```shell
#!/bin/bash

# uWSGI启动命令
start_uwsgi() {
    echo "Starting uWSGI..."
    uwsgi --ini /path/to/your/uwsgi.ini  # 指定你的uWSGI配置文件路径
}

# uWSGI停止命令
stop_uwsgi() {
    echo "Stopping uWSGI..."
    killall -s INT uwsgi
}

# uWSGI状态命令
status_uwsgi() {
    echo "Checking uWSGI status..."
    if pgrep -x "uwsgi" > /dev/null
    then
        echo "uWSGI is running."
    else
        echo "uWSGI is not running."
    fi
}

# 根据输入参数执行相应操作
case "$1" in
    start)
        start_uwsgi
        ;;
    stop)
        stop_uwsgi
        ;;
    restart)
        stop_uwsgi
        start_uwsgi
        ;;
    status)
        status_uwsgi
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit 0

```





#### 7、settings的设置

##### 1、允许授权主机的访问

```python
ALLOWED_HOSTS = ['*']
```

##### 2、处理静态文件

把各个包中的静态文件收集到settings.py中定义的STATIC_ROOT目录中

```python
(venv) root@3865u:/www/sgy# python manage.py collectstatic

154 static files copied to '/www/sgy/static'.

```

3、关闭调试模式

```python 
DEBUG=False
```

4、安装相关包





#### 8、nginx 配置

```python
server {
    listen       8080;
    server_name  guotu.sunliguo.com:8080;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8997;
    }
    
    location ^~ /static {
		# 注意static权限问题
        alias /usr/share/nginx/static;

        }
}

```

```python
[root@aliyun ~]# netstat -ntlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:4444          0.0.0.0:*               LISTEN      1347816/sshd: sunli
tcp        0      0 0.0.0.0:22334           0.0.0.0:*               LISTEN      746574/sshd
tcp        0      0 127.0.0.1:8997          0.0.0.0:*               LISTEN      1398925/uwsgi
tcp        0      0 127.0.0.1:3333          0.0.0.0:*               LISTEN      1347816/sshd: sunli
tcp        0      0 127.0.0.1:9000          0.0.0.0:*               LISTEN      652092/php-fpm: mas
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      332263/nginx: maste
tcp        0      0 127.0.0.1:5553          0.0.0.0:*               LISTEN      1286001/sshd: sunli
tcp        0      0 127.0.0.1:5554          0.0.0.0:*               LISTEN      1286001/sshd: sunli
tcp        0      0 127.0.0.1:53305         0.0.0.0:*               LISTEN      1292337/sshd: sunli
tcp        0      0 127.0.0.1:53306         0.0.0.0:*               LISTEN      1292337/sshd: sunli
tcp6       0      0 :::3306                 :::*                    LISTEN      796676/mysqld
tcp6       0      0 :::80                   :::*                    LISTEN      332263/nginx: maste
[root@aliyun ~]#

```

#### 常见问题：

##### 1、启动uwsgi出现no internal routing support, rebuild with pcre support


需要注意的是pip install uwsgi 要加上–no-cache-dir，pip 可以强制下载重新编译安装的库，不然pip会直接从缓存中拿出了上次编译后的 uwsgi 文件，并没有重新编译一份。

ubuntu环境下
pip uninstall uwsgi

sudo apt-get install libpcre3 libpcre3-dev

pip install uwsgi --no-cache-dir

centos环境下
pip uninstall uwsgi
yum install -y pcre pcre-devel pcre-static
pip install uwsgi --no-cache-dir

##### 2、static 403 问题  权限问题



```python
2022/12/18 22:01:01 [error] 1399687#0: *1613824 open() "/root/ITAM/static/js/jquery-3.6.1.min.js" failed (13: Permission denied), client: 223.97.151.137, server: guotu.sunliguo.com:8080, request: "GET /static/js/jquery-3.6.1.min.js HTTP/1.1", host: "blog.sunliguo.com:8080", referrer: "http://blog.sunliguo.com:8080/computer/list/"

```

```python
#配置nginx上传文件最大限制
client_max_ody_size 50m;
```

```python
2022/12/18 22:23:49 [error] 1400074#0: *1613981 client intended to send too large body: 64673387 bytes, client: 223.97.151.137, server: guotu.sunliguo.com:8080, request: "POST /ip/multi/ HTTP/1.1", host: "blog.sunliguo.com:8080", referrer: "http://blog.sunliguo.com:8080/ip/list/"

```

##### 3、uWSGI running as root, you can use --uid/--gid/--chroot options

```python
修改uWSGI的配置文件，增加如下内容：

uid = www-data 
gid = www-data
这里指定了实例的配置中设置UID和GID，可以解除这个告警。
```

##### 4、chdir(): Permission denied [core/uwsgi.c line 2625

##### 5、--- no python application found, check your startup logs for errors ---

```python
 File "/www/venv/lib/python3.9/site-packages/django/db/backends/mysql/base.py", line 15, in <modu
le>
    import MySQLdb as Database
ModuleNotFoundError: No module named 'MySQLdb'

```



__init__.py

 import pymysql
pymysql.install_as_MySQLdb() 

6、AttributeError at /shoujihao/list/

```
'str' object has no attribute 'utcoffset'
```

```python
root@3865u:~# mysql_tzinfo_to_sql /usr/share/zoneinfo/|mysql -uroot -p mysql
Enter password:
Warning: Unable to load '/usr/share/zoneinfo//leap-seconds.list' as time zone. Skipping it.
Warning: Unable to load '/usr/share/zoneinfo//leapseconds' as time zone. Skipping it.
Warning: Unable to load '/usr/share/zoneinfo//tzdata.zi' as time zone. Skipping it.

```

