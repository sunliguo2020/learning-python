# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeepimgproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_src = scrapy.Field()
