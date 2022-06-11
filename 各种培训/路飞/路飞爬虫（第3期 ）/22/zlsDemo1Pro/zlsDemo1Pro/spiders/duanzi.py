import scrapy
import redis
from ..items import Zlsdemo1ProItem
class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ['https://ishuo.cn/']
    #Redis的链接对象
    conn = redis.Redis(host='127.0.0.1',port=6379)

    def parse(self, response):
        li_list = response.xpath('//*[@id="list"]/ul/li')
        for li in li_list:
            content = li.xpath('./div[1]/text()').extract_first()
            title = li.xpath('./div[2]/a/text()').extract_first()
            all_data = title+content
            #生成该数据的数据指纹
            import hashlib  # 导入一个生成数据指纹的模块
            m = hashlib.md5()
            m.update(all_data.encode('utf-8'))
            data_id = m.hexdigest()

            ex = self.conn.sadd('data_id',data_id)
            if ex == 1:#sadd执行成功（数据指纹在set集合中不存在）
                print('有最新数据的更新，正在爬取中......')
                item = Zlsdemo1ProItem()
                item['title'] = title
                item['content'] = content
                yield item
            else:#sadd没有执行成功（数据指纹在set集合中存储）
                print('暂无最新数据更新，请等待......')




