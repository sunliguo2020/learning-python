# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/8 17:40
"""
import csv
import datetime
import os

from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pageination import Pagination

from django.conf import settings
from app01.utils.encrypt import file_md5sum
from app01.utils.insertdb_blob import file_blob

from app01.utils.form import UploadWebcamModelForm


def webcam_list(request):
    """
    显示图片列表
    :param request:
    :return:
    """
    queryset = models.WebcamPic.objects.all()
    page_object = Pagination(request, queryset)

    form = UploadWebcamModelForm()
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        'form': form,
    }

    return render(request, 'webcam/webcam_list.html', context)


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
                models.WebcamPic.objects.create(file_name=each_file, md5sum=md5sum, blob=blob, mod_time=mod_time)
            # break

    return HttpResponse('插入数据库成功!')


def upload(request):
    """
    上传监控截图
    :param request:
    :return:
    """
    if request.method == "GET":
        form = UploadWebcamModelForm()
        return render(request, 'webcam/webcam_upload.html', {"form": form})
    form = UploadWebcamModelForm(request.POST, request.FILES)

    if form.is_valid():
        # print(form.cleaned_data)
        """
        {'file_name': '33', 'img': <InMemoryUploadedFile: WIN_20221202_19_17_52_Pro.jpg (image/jpeg)>, 'create_datetime': datetime.datetime(2022, 12, 11, 20, 4)}
        """
        # print(form.instance) #WebcamPic object (None)
        # print(form.cleaned_data) #{'img': <InMemoryUploadedFile: WIN_20221202_19_17_52_Pro.jpg (image/jpeg)>}
        # print(form.cleaned_data.get('img'))

        # 不用用户输入文件名
        form.instance.file_name = form.cleaned_data.get('img')
        form.save()
    return redirect('/webcam/list/')


def webcam_delete(request, nid):
    models.WebcamPic.objects.filter(id=nid).delete()
    return redirect('/webcam/list/')
