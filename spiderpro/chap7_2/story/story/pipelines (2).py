# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StoryPipeline:
    def __init__(self):
        self.story_file = open('./story.txt', 'w', encoding='utf-8')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.story_file.close()

    def process_item(self, item, spider):
        #print(type(item['content']))
        info = ''.join(item['title'])+'\t'+item['content']+'\n'
        self.story_file.write(info)
        return item
