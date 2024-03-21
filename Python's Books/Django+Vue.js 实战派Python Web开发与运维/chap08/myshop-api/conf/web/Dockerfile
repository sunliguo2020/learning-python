#基础镜像，基于centos7.9版本构建
FROM centos:7.9.2009
#维护者信息
MAINTAINER yangcoder 111@111.com
#安装Python3.8.2环境，Django3.1.5环境
#安装gunicorn环境。
#安装项目需要环境。
ADD Python-3.8.2.tgz /opt
#安装依赖
RUN yum install yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel gcc pcre pcre-devel zlib automake autoconf libtool make
#切换目录
WORKDIR /opt/Python-3.8.2
#指定安装目录并编译安装
RUN ./configure --prefix=/usr/local/python3.8 && make && make install
#创建软链接
RUN ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python3
RUN ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip3
#创建目录
RUN mkdir -p /home/yang/myshop-api
#切换到工作目录
WORKDIR /home/yang/myshop-api
#将当前目录加入到工作目录
ADD . /home/yang/myshop-api
#安装依赖的包
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
#映射端口
EXPOSE 8002
#运行命令
CMD ["sh","start.sh"]