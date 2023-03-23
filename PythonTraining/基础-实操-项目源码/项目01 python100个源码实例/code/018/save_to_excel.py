import requests
import xlsxwriter

def get_json(index):
    # 爬虫功能
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
        "content-type": "application/json",
        "origin": "https://study.163.com",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

    try:
        response = requests.post(url,json=payload,headers=headers)
        content = response.json()
        if content and content["code"] == 0:
            return content
        return None

    except:
        print("出错了")

def get_course(content):
    course_list = content["result"]["list"]
    return course_list


def save_excel(course_list):
    # 填充爬取的课程信息
    # page1  行数 1 50     50*(1-1) + 1
    # page2  行数 51 100   50*(2-1) + 1
    # page3  行数 101 150  50*(3-1) + 1
    for num,course in enumerate(course_list):
        row = 50*(index-1)+ num+1
        worksheet.write(row, 0, course["productId"])
        worksheet.write(row, 1, course["courseId"])
        worksheet.write(row, 2, course["productName"])
        worksheet.write(row, 3, course["provider"])
        worksheet.write(row, 4, course["score"])
        worksheet.write(row, 5, course["learnerCount"])
        worksheet.write(row, 6, course["lectorName"])
        worksheet.write(row, 7, course["originalPrice"])
        worksheet.write(row, 8, course["discountPrice"])
        worksheet.write(row, 9, course["bigImgUrl"])
        worksheet.write(row, 10, course["description"])

def main(index):
    content = get_json(index)         # 获取json数据
    course_list = get_course(content) # 获取第index页的50条件记录
    save_excel(course_list)           # 写入到excel

if __name__ == "__main__":

    # 存入excel
    workbook = xlsxwriter.Workbook("网易云课堂Python课程数据.xlsx")  # 创建excel
    worksheet = workbook.add_worksheet("first_sheet")
    worksheet.write(0, 0, "商品id")
    worksheet.write(0, 1, "课程id")
    worksheet.write(0, 2, "课程名称")
    worksheet.write(0, 3, "机构名称")
    worksheet.write(0, 4, "评分")
    worksheet.write(0, 5, "学习人数")
    worksheet.write(0, 6, "讲师名称")
    worksheet.write(0, 7, "原价")
    worksheet.write(0, 8, "折扣价")
    worksheet.write(0, 9, "图片")
    worksheet.write(0, 10, "课程描述")

    total_page_count = get_json(1)["result"]["query"]["totlePageCount"] # 总页数
    for index in range(1,total_page_count+1):
        main(index)
    workbook.close()
