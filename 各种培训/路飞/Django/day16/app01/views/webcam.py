# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/8 17:40
"""
import csv
import datetime
import os

from django.shortcuts import render,HttpResponse
from app01 import models
from app01.utils.pageination import Pagination

from django.conf import settings
from app01.utils.encrypt import file_md5sum
from app01.utils.insertdb_blob import file_blob


def webcam_list(request):
    """
    显示图片列表
    :param request:
    :return:
    """
    queryset = models.Webcam.objects.all()

    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    # 测试Django读取本地文件,注意路径问题
    csv_rows = []
    webcam_pic_dir = os.path.join(settings.BASE_DIR, 'app01/static/webcam')
    for root, dirs, files in os.walk(webcam_pic_dir):
        for item in files:
            file_name = item
            file_path = os.path.join(root, item).replace('./static/webcam', "")
            print(file_path)
            ipaddr = file_name.split('_')[0]
            print(ipaddr)
            capture_time_str = file_name.split('_')[4]
            # print(capture_time)
            capture_time = datetime.datetime.strptime(capture_time_str, '%Y%m%d%H%M%S')
            print(capture_time)
            csv_rows.append((ipaddr, file_name, capture_time, file_name))

        with open('./webcam.csv', 'w', newline='') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerows(csv_rows)

    return render(request, 'webcam_list.html', context)


def insert_db(request):
    """将截图插入到数据库中"""

    def webcam_datetime(file_full_name):
        """根据文件名解析出截图的时间
        172.21.65.169_admin_dahua_rstp_20221106090114_channel_27.jpg
        1、解析出包含日期时间的字符串 20221209081512  14个字符，全是数字，以202开头

        """
        capture_time = datetime.datetime.now()
        file_name = os.path.split(file_full_name)[0]
        for capture_time_str in file_name.split('_'):
            print(capture_time_str)
            if len(capture_time_str) == 14 and capture_time_str.isdigit():
                capture_time = datetime.datetime.strptime(capture_time_str, '%Y%m%d%H%M%S')
                # break

        return capture_time
    webcam_pic_dir = os.path.join(settings.BASE_DIR, 'app01/static/webcam')

    for root, dirs, files in os.walk(webcam_pic_dir):
        for each_file in files:
            file_path = os.path.join(root, each_file)
            md5sum = file_md5sum(file_path)
            blob = file_blob(file_path)
            mod_time = webcam_datetime(each_file)

            if not models.WebcamPic.objects.filter(md5sum=md5sum).exists():
                models.WebcamPic.objects.create(file_name=each_file,md5sum=md5sum,blob=blob,mod_time=mod_time)
            # break

    return HttpResponse('插入数据库成功!')
