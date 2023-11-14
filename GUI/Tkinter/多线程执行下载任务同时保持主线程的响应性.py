# 使用多线程执行下载任务，同时保持主线程的响应性

import tkinter as tk
import threading
import time


def download():
    # 模拟下载任务
    for i in range(1,6):
        result_label.config(text=f"下载中。。。{i}/5")
        # 更新主界面以显示下载进度
        root.update()
        # 模拟下载延迟
        time.sleep(1) 
    result_label.config(text="下载完成！")

root =tk.Tk()
root.title('多线程示例')

download_button = tk.Button(root,text='开始下载',command=download)
download_button.pack()

result_label = tk.Label(root,text='')
result_label.pack()
# 创建一个下载线程，用于执行下载任务
download_thread = None

def start_download_thread():
    global download_thread
    if download_thread is None or not download_thread.is_alive():
        download_thread = threading.Thread(target=download)
        download_thread.start()

download_button = tk.Button(root,text='开始下载',command=start_download_thread)
download_button.pack()


root.mainloop()