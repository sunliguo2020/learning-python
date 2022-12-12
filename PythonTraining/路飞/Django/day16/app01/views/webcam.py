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


def webcam_datetime(file_full_name):
    """根据文件名解析出截图的时间
    172.21.65.169_admin_dahua_rstp_20221106090114_channel_27.jpg
    1、解析出包含日期时间的字符串 20221209081512  14个字符，全是数字，以202开头

    """
    capture_time = datetime.datetime.now()

    # 去掉扩展名
    file_name = os.path.splitext(file_full_name)[0]

    for capture_time_str in file_name.split('_'):

        if len(capture_time_str) == 14 and capture_time_str.isdigit():
            capture_time = datetime.datetime.strptime(capture_time_str, '%Y%m%d%H%M%S')

    return capture_time


def webcam_ip(file_full_name):
    """
    从文件名解析出ip地址
    :param file_full_name:
    :return:
    """
    file_name = os.path.splitext(file_full_name)[0]
    return file_name.split('_')[0]


def webcam_list(request):
    """
    显示图片列表
    :param request:
    :return:
    """
    data_dict = {}
    search_data = request.GET.get('q', "")

    if search_data:
        data_dict['file_name__contains'] = search_data

    queryset = models.WebcamPic.objects.filter(**data_dict).order_by("-capture_datetime")
    page_object = Pagination(request, queryset)

    form = UploadWebcamModelForm()
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        'form': form,
        'search_data': search_data,
    }

    return render(request, 'webcam/webcam_list.html', context)


def insert_db(request):
    """将截图插入到数据库中"""

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

    form = UploadWebcamModelForm(data=request.POST, files=request.FILES)

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
        # 判断文件名是否已经存在，没有找到提示错误的方法
        if not models.WebcamPic.objects.filter(file_name=form.cleaned_data.get('img')).exists():
            print(type(form.instance.file_name))
            form.instance.capture_datetime = webcam_datetime(str(form.instance.file_name))
            form.instance.ip_addr = webcam_ip(str(form.instance.file_name))
            form.save()
        else:
            print('文件名已经存在')
    return redirect('/webcam/list/')


def webcam_delete(request, nid):
    """
    截图删除记录及文件
    :param request:
    :param nid:
    :return:
    """

    # 删除文件
    file_path = models.WebcamPic.objects.filter(id=nid).values('img')
    print(file_path[0].get('img'))
    file_full_path = os.path.join(settings.MEDIA_ROOT, file_path[0].get('img'))
    if os.path.isfile(file_full_path):
        os.remove(file_full_path)
    # 删除截图记录
    models.WebcamPic.objects.filter(id=nid).delete()
    return redirect('/webcam/list/')
