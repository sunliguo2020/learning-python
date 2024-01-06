# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-17 13:07
"""
import os


class FilePath:
    def __init__(self, path):
        self.path = path

    def get_basename(self):
        """
        获取文件名
        """
        return self.path.split(os.sep)[-1]

    @property
    def basename(self):
        return self.path.rsplit(os.sep, 1)[-1]

    @basenaem.settr
    def basename(self, name):
        """修改当前路径里的文件名部分"""
        new_path = self.path.rsplit(os.sep, 1)[:-1] + [name]
        self.path = os.sep.join(new_path)

    @basename.deleter
    def basename(self):
        raise RuntimeError('Can not delete basename!')


if __name__ == '__main__':
    p = FilePath(r'c:\user\a.jpg')
    print(p.basename)
