from bs4 import BeautifulSoup

# 实例化soup对象
soup = BeautifulSoup(open('douban.html', 'r', encoding='utf-8'), 'lxml')



# print(soup.p.attr)
# # print(soup.div.attr['id'])
# print(type(soup.div))
#
# # print(soup.div['class'])
# #获取文本内容
# print(soup.title)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.title.get_text())
#
# #find 方法 只拿到一条
#
# print(soup.find('div'))  #等同于soup.div
#条件筛选
# print(soup.find('div',attrs={'id':'anony-nav-banner'}))

print(soup.find('span',class_='num'))