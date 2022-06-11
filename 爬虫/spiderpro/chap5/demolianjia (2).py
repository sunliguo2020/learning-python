# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/9/13 21:03
"""
import requests
from bs4 import BeautifulSoup
import mysql.connector


class LianJiaSpider():
    def __init__(self):
        self.url = 'http://bj.lianjia.com/chengjiao/pg{0}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}

    def send_request(self, url):
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200:
            return resp

    def pase_html(self, resp):
        html = resp.text
        bs = BeautifulSoup(html, 'lxml')
        ul = bs.find('ul', class_='listContent')
        li_list = ul.find_all('li')
        print(len(li_list))

        for item in li_list:
            title = item.find('div', class_='title').text
            houseInfo = item.find('div', class_='houseInfo').text
            positionInfo = item.find('div', class_='positionInfo').text
            dealDate = item.find('div', class_='dealDate').text
            number = item.find('span', class_='number').text + '万'
            unitPrice = item.find('div', class_='unitPrice').text

            print(title)
            print(unitPrice)

        def save(self):
            pass

    def start(self):
        for i in range(1, 2):
            full_url = self.url.format(i)
            resp = self.send_request(full_url)
            # print(resp.text)
            self.pase_html(resp)


if __name__ == "__main__":
    lianjia = LianJiaSpider()
    lianjia.start()
