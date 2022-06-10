import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal


#

class NewTaskThread(QThread):
    # 信号，触发信号，更新窗体中的数据
    success = pyqtSignal(int, str, str, str)
    error = pyqtSignal(int, str, str, str)

    def __init__(self, row_index, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row_index = row_index
        self.asin = asin

    def run(self):
        """ 具体线程应该做的事"""
        try:
            res = requests.get(
                url="https://www.amazon.com/gp/product/{}/".format(self.asin),
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                    "pragma": "no-cache",
                    "upgrade-insecure-requests": "1",
                    "cache-control": "no-cache",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                    "accept-encoding": "gzip, deflate, br",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                }
            )
            if res.status_code != 200:
                raise Exception("初始化失败")
            soup = BeautifulSoup(res.text, 'lxml')
            print(soup.find(id="productTitle"))
            title = soup.find(id="productTitle").text.strip()
            tpl = "https://www.amazon.com/gp/product/ajax/ref=dp_aod_ALL_mbc?asin={}&m=&qid=&smid=&sourcecustomerorglistid=&sourcecustomerorglistitemid=&sr=&pc=dp&experienceId=aodAjaxMain"
            url = tpl.format(self.asin)
            # 获取到title和url，将这个信息填写到 表格上 & 写入文件中。
            self.success.emit(self.row_index, self.asin, title, url)
        except Exception as e:
            print(e)
            title = "监控项 {} 添加失败。".format(self.asin)
            self.error.emit(self.row_index, self.asin, title, str(e))
