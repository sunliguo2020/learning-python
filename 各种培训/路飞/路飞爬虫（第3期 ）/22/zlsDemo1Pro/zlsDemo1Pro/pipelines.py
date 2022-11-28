# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Zlsdemo1ProPipeline:
    def process_item(self, item, spider):
        conn = spider.conn
        #保证redis模块的版本是2.10.6
        #pip install redis==2.10.6
        conn.lpush('duanziLib',item)
        return item
