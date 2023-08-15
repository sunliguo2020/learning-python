# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-08-14 13:02
多态：调用对象方法的时候，要看这个对象是父类创建的对象还是子类创建的对象，而不一定非得调用父类或者子类。

1、看上去调用的是相同的方法，但实际上要看这个对象是父类还是子类创建的对象
2、如果是父类创建的对象，一定调用父类中定义的方法。
3、如果是子类创建的对象，那么就要看子类中是否重写了父类的方法。
    如果子类重写了父类的方法，那么会调用子类的方法
    如果子类没有重写了父类的方法，那么会调用父类的方法

"""


class MiniOS:
    """MiniOS操作系统类"""

    def __init__(self, name):
        self.name = name
        self.apps = []  # 安装的应用程序名称列表

    def __str__(self):
        return f"{self.name}安装的软件列表为{self.apps}"

    def install_app(self, app):
        # 判断是否已经安装了软件
        if app.name in self.apps:
            print(f"已经安装了{app.name},无需再次安装!")
        else:
            app.install()
            self.apps.append(app.name)


class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return f"{self.name}的当前版本是{self.version}-{self.desc}"

    def install(self):
        print(f"将{self.name}[{self.version}]的执行程序复制到程序目录....")


class PyCharm(App):
    pass


class Chrome(App):
    def install(self):
        print("正在解压缩安装程序...")
        super().install()


linux = MiniOS("Linux")
print(linux)

pycharm = PyCharm("PyCharm", '1.0', "python开发的IDE环境")
chrome = Chrome('Chrome', '2.0', '谷歌浏览器')

linux.install_app(pycharm)
linux.install_app(chrome)
linux.install_app(chrome)

print(linux)
