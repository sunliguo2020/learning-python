# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class MycwpjtPipeline:
    fp = None

    def open_spider(self, spider):
        self.fp = open("./sohu.txt", 'w', encoding='utf-8')

    def process_item(self, item, spider):
        name = item['name']
        link = item['link']
        print('-' * 50)
        if name or link:
            data = str(name) + str(link) + "--" * 50 + '\n'
            self.fp.write(data)
        return item

    def close_spider(self, spider):
        self.fp.close()
