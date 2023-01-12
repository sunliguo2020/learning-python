# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PagesproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    src = scrapy.Field()
