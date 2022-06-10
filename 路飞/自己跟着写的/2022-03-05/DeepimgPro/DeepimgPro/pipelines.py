# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DeepimgproPipeline:
    def process_item(self, item, spider):
        return item

#自定的管道类继承ImagesPipeline
class ImgDeepproPipeline(ImagesPipeline):
    #根据图片地址对其发起请求，获取图片数据
    def get_media_requests(self, item, info):
        img_src = item['img_src']
        yield scrapy.Request(img_src)

    #指定图片的名称，（只需要返回图片存储的名称即可
    def file_path(self, request, response=None, info=None, *, item=None):
        img_name = request.url.split('/')[-1]
        return img_name


    def item_completd(self, item):
        return item
