# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class DuanziPipeline:
    fp = None

    def open_spider(self, spider):
        print("我是open_spider 方法，在开始的时候只运行一次。")
        self.fp = open("./data.txt", 'w',encoding='utf-8')

    def process_item(self, item, spider):
        print(item)
        self.fp.write(str(item)+'\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
