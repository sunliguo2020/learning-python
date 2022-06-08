# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class AutopjtPipeline:
    def __init__(self):
        self.fp = open('dangdang.csv','w',encoding='utf-8',newline='')
        self.csv_write =csv.writer(self.fp)


    def process_item(self, item, spider):
        #print(item)
        name = item['name']
        price = item['price']
        link = item['link']
        comnum   = item['comnum']
        #print(name)
        self.csv_write.writerow((name,price,link,comnum))
        print('爬取完成')
        return item
    def close_pider(self,spider):
        self.fp.close()
