# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SavedataproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #爬取的字段有哪些，这里就需要定义哪些变量存储爬取到的字段
    title = scrapy.Field()
    content = scrapy.Field()

