import tkinter.messagebox # 导入tkinter模块的子模块messagebox

# 带一个确定按钮的提示消息框
tkinter.messagebox.showinfo("提示：","愿你的青春不负梦想！")

# 带一个确定按钮的警告消息框
tkinter.messagebox.showwarning("警告：","熊出没！小心！！！")

# 带一个确定按钮的错误消息框
tkinter.messagebox.showerror("错误：","您的操作有误，请重头再来！")

# 带确定和取消按钮的询问对话框
result = tkinter.messagebox.askokcancel("询问对话框：","你确定要清空聊天记录吗？")
print("询问结果：",result)

# 带是和否按钮的询问对话框
result = tkinter.messagebox.askquestion("询问：","您知道洛杉矶凌晨四点钟是什么样子吗？")
print("询问结果：",result)

# 带重试和取消按钮的询问对话框
result = tkinter.messagebox.askretrycancel("询问：","挑战失败，要再试一次吗？")
print("询问结果：",result)


