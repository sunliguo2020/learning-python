# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/25 7:39
"""
import scrapy
class BookSpider(scrapy.Spider):
    name = "books"
    start_urls= ['http://books.toscrape.com']

    def parse(self,response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            #price = book.xpath('./p[@class="price_color"]/text').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {
                "name":name,
                "price":price,
            }
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        print(next_url)
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)