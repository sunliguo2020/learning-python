# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-07-23 15:09
"""


class Ftp():
    def put(self):
        print("正在上传数据！")

    def get(self):
        print("正在下载数据！")

    def interact(self):
        opt = input(">>>>")

        # if hasattr(self, opt):
        #     getattr(self, opt)()
        # else:
        #     print("没有这个功能")
        getattr(self, opt, self.warning)()

    def warning(self):
        print("没有这个功能")


if __name__ == '__main__':
    obj = Ftp()
    obj.interact()
