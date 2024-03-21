import gevent
from gevent import monkey
monkey.patch_all()
import multiprocessing
#预加载资源
preload_app = True
workers = 5 # 并行工作进程数
threads = 4 # 指定每个工作者的线程数
bind = '0.0.0.0:8002' # 端口 8002
# 设置守护进程,将进程交给supervisor管理
daemon = False
worker_class = 'gevent' # 工作模式协程
worker_connections = 2000 # 设置最大并发量
proc_name = 'myshop-api' #设置进程名
pidfile = '/home/yang/myshop-api/gunicorn.pid' # 设置进程文件目录
# 设置访问日志和错误信息日志路径
accesslog = "/home/yang/myshop-api/access.log"
errorlog = "/home/yang/myshop-api/error.log"
loglevel = "debug"
# 设置日志记录水平 
#loglevel = 'warning'
