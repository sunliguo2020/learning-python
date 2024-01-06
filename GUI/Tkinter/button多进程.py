import tkinter as tk
import multiprocessing as mp

def process_task():
    # 这里是子进程的代码，用于执行具体的任务
    # 在这个示例中，我们只是简单地打印一条消息
    print("子进程正在执行任务")

def button_callback():
    # 创建一个新的进程来执行任务
    process = mp.Process(target=process_task)
    process.start()

if __name__ == "__main__":
    
    mp.freeze_support()
    # 创建Tkinter窗口
    window = tk.Tk()

    # 创建按钮并绑定回调函数
    button = tk.Button(window, text="开始任务", command=button_callback)
    button.pack()

    # 进入主循环
    window.mainloop()
