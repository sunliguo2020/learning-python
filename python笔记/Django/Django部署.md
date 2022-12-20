#### uwsgi 配置文件

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

#### uwsgi常用命令

```python
启动：uwsgi --ini  uwsgi.ini
重启： uwsgi --reload uwsgi.pid
停止： uwsgi --stop uwsgi.pid
```

##### static 403 问题  权限问题



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

#### nginx 配置

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

