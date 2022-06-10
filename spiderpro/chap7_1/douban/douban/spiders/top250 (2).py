# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/10/3 18:16
"""
import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'  # 定义允许爬虫爬取的域名
    allowed_domains = ['book.douban.com/top250']
    start_urls = ['https://book.douban.com/top250']

    # parse是scrapy是默认的处理response的一个方法
    def parse(self, response):
        # print(response.text)
        bs = BeautifulSoup(response.text, 'html.parser')
        tr_tag = bs.find_all('tr', class_='item')
        for tr in tr_tag:
            # print(tr)
            book = DoubanItem()
            title = tr.find_all('a')[1]['title']
            publish = tr.find('p', class_='pl').text
            score = tr.find('span', class_='rating_nums').text
            #测试打印输出
            print([title, publish, score])

            book['title'] = title
            book['publish'] = publish
            book['score'] = score

            #数据封装完毕后，提交给spider引擎

            yield book
