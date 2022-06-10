# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from aip import AipNlp
from time import sleep
class WangyiproPipeline:
    client = None
    def open_spider(self,spider):
        """ 你的 APPID AK SK """
        APP_ID = 'xxx'
        API_KEY = 'x'
        SECRET_KEY = 'xx'

        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    #讲每一条新闻的类型进行提取然后打印输出
    def process_item(self, item, spider):
        try:
            title = item['title']
            content = item['content']
            #提取文章类型
            result = self.client.topic(title, content)
            class_new = result['item']['lv1_tag_list'][0]['tag']
            sleep(2)
            print(class_new)
        except Exception as e:
            print('pass')
        return item
