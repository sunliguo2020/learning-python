# _*_ coding:utf-8   _*_
# 文件名称：tools.py.py
# 开发工具：PyCharm

import base64


def handle_jpg_to_py(picture_name):
    """
    将JPG图像文件转换为.py文件
    :param picture_name:图片名称
    """
    open_jpg = open("%s.gif" % picture_name, 'rb')
    b64str = base64.b64encode(open_jpg.read())
    open_jpg.close()
    # 注意b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name, 'w+')
    f.write(write_data)
    f.close()

if __name__ == '__main__':
    picture = ['tmp']
    for pictrue_position in picture:
        handle_jpg_to_py(pictrue_position)
