#基础镜像，基于centos7.9版本构建
FROM centos:7
#维护者信息
MAINTAINER yangcoder 111@111.com
#安装依赖
RUN yum install -y gcc pcre pcre-devel zlib zlib-devel automake autoconf libtool make
#copy-nginx包
ADD nginx-1.18.0.tar.gz /opt
#切换工作目录
WORKDIR /opt/nginx-1.18.0
#指定安装目录并编译安装
RUN ./configure --prefix=/usr/local/nginx && make && make install
#创建软链接
RUN ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx
#copy本地的nginx配置文件到容器
COPY nginx.conf /usr/local/nginx/conf/nginx.conf
#映射端口
EXPOSE 82
#运行命令
CMD nginx 