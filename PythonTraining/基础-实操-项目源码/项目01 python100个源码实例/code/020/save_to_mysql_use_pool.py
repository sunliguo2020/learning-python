import requests
import time
import pymysql
from multiprocessing import Pool

#连接数据库
conn = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                passwd='root',
                db='spider',
                charset='utf8')
cur = conn.cursor()

def get_json(index):
    """
    爬取课程的Json数据
    :param index: 当前索引,从0开始
    :return: Json数据
    """
    url = "https://study.163.com/p/search/studycourse.json"
    payload = {
        "activityId": 0,
        "keyword": "python",
        "orderType": 5,
        "pageIndex": index,
        "pageSize": 50,
        "priceType": -1,
        "qualityType": 0,
        "relativeOffset": 0,
        "searchTimeType": -1,
    }

    headers = {
        "accept": "application/json",
        "host": "study.163.com",
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    try:
        # 发送POST请求
        response = requests.post(url,json=payload,headers=headers)
        # 获取JSON数据
        content_json = response.json()
        if content_json and content_json["code"] == 0:
            return content_json
        return None
    except Exception as e:
        print('出错了')
        print(e)
        return None

def get_content(content_json):
    """
    获取课程信息列表
    :param content_json: 获取的Json格式数据
    :return: 课程数据
    """
    if "result" in content_json:
        return content_json["result"]["list"]

def check_course_exit(course_id):
    """
    检查课程是否存在
    :param course_id: 课程id
    :return: 课程存在返回True,否则返回False
    """
    # 根据course_id查找course表中记录
    sql = f'select course_id from course where course_id = {course_id}'
    # 执行SQL语句
    cur.execute(sql)
    # 查找一条记录
    course = cur.fetchone()
    # 如果数据库中存在，返回True;否则，返回False。
    if course:
        return True
    else:
        return False

def save_to_course(course_data):
    """
    保存到course表
    :param course_data: 元组数据
    :return: None
    """
    sql_course = """insert into course
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    # exetemany方法插入多条记录
    cur.executemany(sql_course, course_data)

def save_mysql(content):
    """
    保存到MySQL
    :param content: 爬取的数据
    :return:
    """
    course_data = []
    # 遍历课程列表
    for item in content:
        # 如果数据表中没有该条记录，则保留
        if not check_course_exit(item['courseId']):
            # 加入元组
            course_value = (item['courseId'],item['productName'],item['provider'],item['score'],item['learnerCount'],
                             item['lessonCount'],item['lectorName'],item['originalPrice'], item['discountPrice'],
                             item['discountRate'],item['imgUrl'], item['bigImgUrl'],
                             item['description'],)
            course_data.append(course_value)
    # 调用save_to_course方法，写入数据库
    save_to_course(course_data)

def main(index):
    # 获取JSON格式数据
    content_json = get_json(index)
    # 获取课程内容
    content = get_content(content_json)
    # 保存到数据库
    save_mysql(content)

if __name__ == '__main__':
    print('开始执行')
    start = time.time() # 记录开始时间
    # 获取总页数
    totlePageCount = get_json(1)['result']["query"]["totlePageCount"]
    # 不使用多进程
    # for index in range(totlePageCount):
    #     main(index)
    # 使用多进程
    pool = Pool() # 开启进程
    index = ([x for x in range(1,totlePageCount+1)]) # 生成当前页码元组
    pool.map(main, index) # 执行多进程
    pool.close() # 关闭进程
    pool.join()  # 等待子进程结束
    cur.close()  # 关闭游标
    conn.commit() # 提交到数据库
    conn.close()  # 关闭数据库连接
    print('执行结束')
    end = time.time() # 记录技术时间
    print(f'程序执行时间是{end-start}秒。') # 输出执行时间
