import scrapy
import redis
from ..items import Zlsdemo2ProItem
class JianliSpider(scrapy.Spider):
    name = 'jianli'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/jianli/free.html']
    conn = redis.Redis(host='127.0.0.1',port=6379)
    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            title = div.xpath('./p/a/text()').extract_first()
            #充当数据指纹
            detail_url = 'https:'+div.xpath('./p/a/@href').extract_first()
            ex = self.conn.sadd('data_id',detail_url)
            item = Zlsdemo2ProItem()
            item['title'] = title
            if ex == 1:
                print('有最新数据的更新，正在采集......')
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
            else:
                print('暂无数据更新！')

    def parse_detail(self,response):
        item = response.meta['item']
        download_url = response.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href').extract_first()
        item['download_url'] = download_url

        yield item