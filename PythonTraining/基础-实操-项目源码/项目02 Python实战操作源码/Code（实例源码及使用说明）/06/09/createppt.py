# -*- coding: UTF-8 -*-
from win32com.client import Dispatch  # 导入pywin32模块的client包下的函数
import os   # 导入系统功能模块


'''批量生成PowerPoint演示文稿中的幻灯片'''
def PowerPoint():
    ppt = os.path.join(os.getcwd(), "titles.pptx")  # 片头模板文件
    App = Dispatch("PowerPoint.Application")  # 创建PowerPoint应用程序
    App.Visible = True  # 显示PowerPoint窗口
    Presentation = App.Presentations.Open(ppt)  # 打开模板文件
    itemlist = [("《半壶纱》", "宋佳琦"), ("《洞庭新歌》", "Aurora"), ("《知否、知否》", "无语")]  # 要显示的内容列表
    itemlen = len(itemlist)  # 节目的个数
    offset = 2  # 设置新添加幻灯片的起始页，值为：模板的片头幻灯片个数+1
    for n in range(offset, itemlen + offset):  # 复制和曲目相同个数的幻灯片（由于要保留格式，所以此处只能通过合并PPT的方式实现）
        # 将当前目录下的page.pptx中的幻灯片插入到当前PPT文件中
        Presentation.Slides.InsertFromFile(os.path.join(os.getcwd(), "page.pptx"), Presentation.Slides.Count, 1, 1)
    for i in range(offset, itemlen + offset):  # 循环修改每页幻灯片中的曲目名称和表演者
        item = itemlist[i - 2]
        Presentation.Slides(i).Shapes(1).TextFrame.TextRange.Text = item[0]  # 修改第一个文本框的内容
        Presentation.Slides(i).Shapes(2).TextFrame.TextRange.Text = "表演者：" + item[1]  # 修改第二个文本框的内容
    outfile = os.path.join(os.getcwd(), "音乐会PPT.pptx")   # 目标文件
    Presentation.SaveAs(outfile)  # 另存为新的PowerPoint演示文稿
    App.Quit()  # 退出PowerPoint
    print("PPT文件已生成！文件位置为：",outfile)
PowerPoint()  # 调用函数开始生成


