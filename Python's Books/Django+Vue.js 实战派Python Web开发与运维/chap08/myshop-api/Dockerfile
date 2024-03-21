#基础镜像，基于python3.8.2版本构建
FROM python:3.8.2
#维护者信息
MAINTAINER yangcoder 111@111.com
#创建目录
RUN mkdir -p /home/yang/myshop-api
#切换到工作目录
WORKDIR /home/yang/myshop-api
#将当前目录加入到工作目录
ADD . /home/yang/myshop-api
#安装依赖的包
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#映射端口
EXPOSE 8005
#执行命令
CMD ["gunicorn", "-c", "gunicorn.py","myshop.wsgi:application"]