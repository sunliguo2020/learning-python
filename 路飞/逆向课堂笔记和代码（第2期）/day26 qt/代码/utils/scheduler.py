class Scheduler(object):
    def __init__(self):
        self.thread_list = []

    def start(self):
        # 1.获取表格中的所有数据，每一行创建一个线程去执行监控
        # 2.每个线程 执行 & 状态实时的显示在表格中 信号+回调
        pass

    def stop(self):
        pass


# 单例模式
SCHEDULER = Scheduler()
