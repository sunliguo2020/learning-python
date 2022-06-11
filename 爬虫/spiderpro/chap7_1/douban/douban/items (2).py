# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publish = scrapy.Field()
    score = scrapy.Field()

#测试
# book =DoubanItem()
# book['titl2e']='红楼梦'
# print(book)
# print(dir(book))
# print(type(book))
