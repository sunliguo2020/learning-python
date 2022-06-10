# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/3/20 8:17
"""
import os.path

import exifread


def img_exif_read(file_path):
    exif_process_dict = {}
    with open(file_path, 'rb') as fp:
        try:
            exif_process_dict = exifread.process_file(fp)
        except Exception as e:
            print("读取exif错误：", file_path, e)
        # else:
        #     exif_process_dict = {}
        # pprint.pprint(exif_process)

    return exif_process_dict


if __name__ == '__main__':

    exif_process = img_exif_read('IMG_20200625_112016.jpg')
    # for item, value in exif_process.items():
    #     print(item, value)
    # print("-" * 50)
    # print(exif_process.get('JPEGThumbnail'))

    # with open('thumbnail.jpg', 'wb') as fp:
    #     fp.write(exif_process.get('JPEGThumbnail'))
    img_model = exif_process.get('Image Model')
    if img_model:
        print(img_model)
    for root, dirs, files in os.walk(r'd:\BaiduNetdiskDownload'):
        for f in files:

            file_path = os.path.join(root, f)
            #print(file_path)
            exif_process = img_exif_read(file_path)
            img_model = exif_process.get('Image Model')
            if img_model:
                print(file_path, img_model)
