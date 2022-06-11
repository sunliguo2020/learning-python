### 管道深入操作

- 如何将数据存储到数据库

  - 注意：一个管道类负责将数据存储到一个具体的载体中。如果想要将爬取到的数据存储到多个不同的载体/数据库中，则需要定义多个管道类。

- 思考：

  - 在有多个管道类的前提下，爬虫文件提交的item会同时给没一个管道类还是单独的管道类？
    - 爬虫文件只会将item提交给优先级最高的那一个管道类。优先级最高的管道类的process_item中需要写return item操作，该操作就是表示将item对象传递给下一个管道类，下一个管道类获取了item对象，才可以将数据存储成功！

- 管道类：

- ```python
  # Define your item pipelines here
  #
  # Don't forget to add your pipeline to the ITEM_PIPELINES setting
  # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  
  
  # useful for handling different item types with a single interface
  from itemadapter import ItemAdapter
  import pymysql
  import redis
  import pymongo
  #负责将数据存储到mysql中
  class MysqlPipeline:
      conn = None #mysql的链接对象
      cursor = None
      def open_spider(self,spider):
          self.conn = pymysql.Connect(
              host = '127.0.0.1',
              port = 3306,
              user = 'root',
              password = 'boboadmin',
              db = 'spider3qi',
              charset = 'utf8'
          )
          self.cursor = self.conn.cursor()
      #爬虫文件每向管道提交一个item，则process_item方法就会被调用一次
      def process_item(self, item, spider):
          title = item['title']
          sql = 'insert into xiaoshuo (title) values ("%s")'%title
          self.cursor.execute(sql)
          self.conn.commit()
          print('成功写入一条数据！')
          return item
      def close_spider(self,spider):
          self.cursor.close()
          self.conn.close()
  
  #将数据持久化存储到redis中
  class RedisPipeLine:
      conn = None
      def open_spider(self,spider):
          #在链接前务必手动启动redis的服务
          self.conn = redis.Redis(
              host='127.0.0.1',
              port=6379
          )
      def process_item(self,item,spider):
          #注意：如果想要将一个python字典直接写入到redis中，则redis模块的版本务必是2.10.6
          #如果redis模块的版本不是2.10.6则重新安装：pip install redis==2.10.6
          self.conn.lpush('xiaoshuo',item)
          print('数据存储redis成功！')
          return item
  
  class MongoPipeline:
      conn = None #链接对象
      db_sanqi = None #数据仓库
      def open_spider(self,spider):
          self.conn = pymongo.MongoClient(
              host='127.0.0.1',
              port=27017
          )
          self.db_sanqi = self.conn['sanqi']
      def process_item(self,item,spider):
          self.db_sanqi['xiaoshuo'].insert_one({'title':item['title']})
          print('插入成功！')
          return item
  ```

- 配置文件：

- ```
  ITEM_PIPELINES = {
     #数字表示管道类被执行的优先级，数字越小表示优先级越高
     'xiaoshuoPro.pipelines.MysqlPipeline': 300,
     'xiaoshuoPro.pipelines.RedisPipeLine': 301,
     'xiaoshuoPro.pipelines.MongoPipeline': 302,
  }
  ```

### scrapy爬取多媒体资源数据

- 使用一个专有的管道类ImagesPipeline

- 具体的编码流程：

  - 1.在爬虫文件中进行图片/视频的链接提取

  - 2.将提取到的链接封装到items对象中，提交给管道

  - 3.在管道文件中自定义一个父类为ImagesPipeline的管道类，且重写三个方法即可：

    - ```
      def get_media_requests(self, item, info):接收爬虫文件提交过来的item对象，然后对图片地址发起网路请求，返回图片的二进制数据
      
      def file_path(self, request, response=None, info=None, *, item=None)：指定保存图片的名称
      def item_completed(self, results, item, info)：返回item对象给下一个管道类
      ```

  - 4.在配置文件中开启指定的管道，且通过IMAGES_STORE = 'girlsLib'操作指定图片存储的文件夹。

  ```python
  # Define your item pipelines here
  #
  # Don't forget to add your pipeline to the ITEM_PIPELINES setting
  # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  
  
  # useful for handling different item types with a single interface
  import scrapy
  from itemadapter import ItemAdapter
  
  from scrapy.pipelines.images import ImagesPipeline
  
  #自定义的管道类一定要继承与ImagesPipeline
  class mediaPileline(ImagesPipeline):
      #重写三个父类的方法来完成图片二进制数据的请求和持久化存储
      #可以根据图片地址，对其进行请求，获取图片数据
      #参数item：就是接收到的item对象
      def get_media_requests(self, item, info):
          img_src = item['src']
          yield scrapy.Request(img_src)
      #指定图片的名称（只需要返回图片存储的名称即可）
      def file_path(self, request, response=None, info=None, *, item=None):
          imgName = request.url.split('/')[-1]
          print(imgName,'下载保存成功！')
          return imgName
      #如果没有下一个管道类，该方法可以不写
      def item_completed(self, results, item, info):
          return item #可以将当前的管道类接收到item对象传递给下一个管道类2.
  ```

  

### scrapy深度爬取

- 如何爬取多页的数据（全站数据爬取）

  - 手动请求发送：

    - ```
      #callback用来指定解析方法
      yield scrapy.Request(url=new_url,callback=self.parse)
      ```

- 如何爬取深度存储的数据

  - 什么是深度，说白了就是爬取的数据没有存在于同一张页面中。

  - 必须使用请求传参的机制才可以完整的实现。

    - 请求传参：

      - ```
        yield scrapy.Request(meta={},url=detail_url,callback=self.parse_detail)
        
        可以将meta字典传递给callback这个回调函数
        ```

```python
import scrapy
from ..items import DeepproItem

class DeepSpider(scrapy.Spider):
    name = 'deep'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']
    #解析首页数据
    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            detail_url = 'https://wz.sun0769.com'+li.xpath('./span[3]/a/@href').extract_first()
            # print(title)
            item = DeepproItem()
            item['title'] = title
            #对详情页的url发起请求
            #参数meta可以将自身这个字典传递给callback指定的回调函数
            yield scrapy.Request(meta={'item':item},url=detail_url,callback=self.parse_detail)
    #解析详情页数据
    def parse_detail(self,response):
        meta = response.meta #接收请求传参过来的meta字典
        item = meta['item']
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]//text()').extract()
        content = ''.join(content)
        # print(content)
        item['content'] = content

        yield item

```

