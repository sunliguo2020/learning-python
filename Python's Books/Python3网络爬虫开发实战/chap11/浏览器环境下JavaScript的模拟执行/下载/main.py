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
    "/js/chunk-10192a00.243cb8b7.js",
    lambda route: route.fulfill(path="./chunk.js")
)
page.goto(BASE_URL)


def get_token(offset):
    result = page.evaluate('''() => {
        return window.encrypt("%s", "%s")
    }''' % ('/api/movie', offset))
    return result


for i in range(MAX_PAGE):
    offset = i * LIMIT
    token = get_token(offset)
    index_url = INDEX_URL.format(limit=LIMIT, offset=offset, token=token)
    response = requests.get(index_url)
    print('response', response.json())

time.sleep(10)
