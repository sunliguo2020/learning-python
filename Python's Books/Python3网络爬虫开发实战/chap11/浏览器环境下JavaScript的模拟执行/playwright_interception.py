# -*- coding: utf-8 -*-
"""
 @Time : 2024/3/24 12:40
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
from playwright.sync_api import sync_playwright
import time
import requests

BASE_URL = 'https://spa2.scrape.center'
INDEX_URL = BASE_URL + '/api/movie?limit={limit}&offset={offset}&token={token}'

MAX_PAGE = 10
LIMIT = 10

context = sync_playwright().start()
browser = context.chromium.launch(headless=False)
page = browser.new_page()

page.route(
    '**/chunk-10192a00.243cb8b7.js',
    lambda route: route.fulfill(path='./chunk.js')
)
#
# page.route("**/**", lambda route: route.fulfill(
#     content_type="text/plain",
#     body="page not found!"))

page.goto(BASE_URL)


def get_token(offset):
    """

    @param offset:
    @return:
    """
    result = page.evaluate('''
    ()=>{
    return window.encrypt("%s","%s")
    }
    ''' % ('/api/movie', offset))

    return result

    # return page.evaluate('()=>{return window;}')


for i in range(MAX_PAGE):
    offset = i * LIMIT
    token = get_token(offset)
    # print(token)
    index_url = INDEX_URL.format(limit=LIMIT, offset=offset, token=token)
    response = requests.get(index_url)
    print(response.json())

time.sleep(1000)
