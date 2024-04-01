# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/1 21:44
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

INDEX_HTML = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'


def scrape_api(url):
    """

    @param url:
    @return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException as e:
        logging.error('error occurred while scraping %s', url, exc_info=True)


LIMIT = 10


def scrape_index(page):
    """

    @param page:
    @return:
    """
    url = INDEX_HTML.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'


def scrap_detail(id):
    """

    @param id:
    @return:
    """
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


TOTAL_PAGE = 10


def main():
    """

    """
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrap_detail(id)
            logging.info('detail data %s', detail_data)


if __name__ == '__main__':
    main()
