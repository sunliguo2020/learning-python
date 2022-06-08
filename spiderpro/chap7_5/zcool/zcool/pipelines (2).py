# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline
from zcool import settings
import os


class ZcoolPipeline(ImagesPipeline):  # 自定义的用于下载图片的pipeline
    def get_media_requests(self, item, info):
        image_requests = super().get_media_requests(item, info)  # 获取图片链接请求的列表
        print('get_media_requests')
        for img_req in image_requests:

            #print(type(img_req))#<class 'scrapy.http.request.Request'>
            img_req.item = item  # 对每一个图片链接请求都添加一个item属性
        return image_requests

    # 重写这个方法的目的是改变存储路径
    def file_path(self, request, response=None, info=None):

        old_path = super().file_path(request, response, info)
        print("获取图片存储路径加名称",old_path)
        title = request.item['title']
        print('获取到的title:',title)
        save_path = os.path.join(settings.IMAGES_STORE, title)

        print("save_path:",save_path)
        # 提取原路径中的文件名
        image_name = old_path.replace('full/', "")
        return os.path.join(save_path, image_name)
