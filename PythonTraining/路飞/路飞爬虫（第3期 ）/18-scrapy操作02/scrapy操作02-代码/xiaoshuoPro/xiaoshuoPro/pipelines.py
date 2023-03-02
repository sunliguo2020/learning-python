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




