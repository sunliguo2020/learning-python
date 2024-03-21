#python的安装
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
./configure --prefix=/usr/local/python3.8
make && make install
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python3
ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip3

#虚拟环境的安装
pip3 install virtualenv 
ln -s /usr/local/python3.8/bin/virtualenv  /usr/bin/virtualenv
#在“\home\”目录下创建virtualenv目录，该目录是虚拟环境的主目录。
#执行如下命令切换到virtualenv目录下。
virtualenv -p /usr/bin/python3 env-py3.8.2
source env-py3.8.2/bin/activate

#django的安装
pip3 install django==3.1.5
python -m django --version