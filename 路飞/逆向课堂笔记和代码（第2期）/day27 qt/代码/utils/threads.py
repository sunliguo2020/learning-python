import time

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import QThread, pyqtSignal


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


class TaskThread(QThread):
    start_signal = pyqtSignal(int)
    stop_signal = pyqtSignal(int)
    counter_signal = pyqtSignal(int)
    error_counter_signal = pyqtSignal(int)

    def __init__(self, scheduler, log_file_path, row_index, asin, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = scheduler
        self.log_file_path = log_file_path
        self.row_index = row_index
        self.asin = asin

    def run(self):
        # 触发start_signal
        self.start_signal.emit(self.row_index)

        import time
        import random
        while True:
            # 停止
            if self.scheduler.terminate:
                self.stop_signal.emit(self.row_index)
                # 自己的线程在thread_list中移除掉
                self.scheduler.destroy_thread(self)
                return
            try:
                time.sleep(random.randint(1, 3))
                self.counter_signal.emit(self.row_index)

                with open(self.log_file_path, mode='a', encoding='utf-8') as f:
                    f.write("日志\n")

                # 监控的动作
                # 1.根据型号访问通过bs4获取数据
                # 2.获取到数据 价格是否小于预期
                # 3.发送报警（邮件）

                time.sleep(5)
            except Exception as e:
                self.error_counter_signal.emit(self.row_index)


class StopThread(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self, scheduler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler = scheduler

    def run(self):
        # 1.监测线程数量(总线程数）
        while True:
            running_count = len(self.scheduler.thread_list)
            self.update_signal.emit("正在终止({})".format(running_count))
            if running_count == 0:
                break
            time.sleep(1)

        self.update_signal.emit("已终止")
