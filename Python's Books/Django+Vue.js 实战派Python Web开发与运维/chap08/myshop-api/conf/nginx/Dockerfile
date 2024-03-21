#基础镜像，基于nginx最新版
FROM nginx
#维护者信息
MAINTAINER yangcoder 111@111.com
#工作目录
WORKDIR /usr/share/nginx/html/
#创建目录
RUN mkdir -p /usr/share/nginx/html/static && mkdir -p /usr/share/nginx/html/media
#copy本地的nginx配置文件到容器
COPY nginx.conf /etc/nginx/nginx.conf
#copy static目录及其文件
ADD ./static /usr/share/nginx/html/static
ADD ./media /usr/share/nginx/html/media
#映射端口
EXPOSE 85
#运行命令,关闭守护模式
CMD ["nginx", "-g", "daemon off;"]