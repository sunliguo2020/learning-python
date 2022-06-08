import scrapy


class QustorySpider(scrapy.Spider):
    name = 'qustory'
    allowed_domains = ['qu.la']
    start_urls = ['http://qu.la/book/118039/3540856.html']

    def parse(self, response):
        print(dir(response))
        print(response.url)
        print(response.json)
        # title = response.xpath('//h1[@class="title"]/text()').extract()
        # # print(title)
        # content = response.xpath('string(//div[@id="content"])').extract_first().strip()
        # print(title, content)
        # next_url = 'https://www.qu.la/book' + response.xpath(
        #     '//*[@id="container"]/div/div/div[2]/div[1]/a[3]/@href').extract_first()
        # print(next_url)
        #
        # yield {
        #     'title': title,
        #     "content": content
        # }
        # yield scrapy.Request(next_url, callback=self.parse)
