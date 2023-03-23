# _*_ coding:utf-8   _*_
# 文件名称：wordtopdf.py
# 开发工具：PyCharm

from win32com.client import Dispatch  # 导入pywin32模块的client包下的函数
from win32com.client import constants  #  导入pywin32模块的client包下的保存COM常量的类
from win32com.client import gencache    #  导入pywin32模块的client包下的gencache函数
import pythoncom  # 导入封装了OLE自动化API的模块，该模块为pywin32的子模块
import os  # 导入操作系统模块


# 批量替换Word文档中的指定文字，包括页眉中的文字
def replaceall(filelist,targetpath,strold,strnew):
    errmark = False  # 标记是否报错，False表示没有报错，True表示报错
    try:
        pythoncom.CoInitialize()   # 调用线程初始化COM库，解决调用Word 2007时出现“尚未调用CoInitialize”错误的问题
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        w = Dispatch("Word.Application")  # 创建Word应用程序
        w.DisplayAlerts = 0 # 后台运行不显示、不警告
        for fullfilename in filelist:
            # 文档路径需要为绝对路径，因为Word启动后当前路径不是调用脚本时的当前路径。
            try:
                doc = w.Documents.Open(fullfilename)  # 打开Word文件
                filepath,fullname = os.path.split(fullfilename)  # 从绝对路径中分割路径和完整文件名
                fname,ext = os.path.splitext(fullname)   # 从完整文件名中分割文件名和扩展名
                targetfile = os.path.abspath(targetpath+"\\" + fname +".docx") # 组合目标文件绝对路径
                doc.Content.Find.Execute(FindText= strold,ReplaceWith=strnew,Replace=2)  # 替换正文中的内容
                '''
                替换页眉
                '''
                w.ActiveDocument.Sections(1).Headers(constants.wdHeaderFooterPrimary).Range.Find.ClearFormatting()
                w.ActiveDocument.Sections(1).Headers(constants.wdHeaderFooterPrimary).Range.Find.Replacement.ClearFormatting()
                w.ActiveDocument.Sections(1).Headers(constants.wdHeaderFooterPrimary).Range.Find.\
                            Execute(FindText = strold,MatchCase = False,MatchWholeWord = False,MatchWildcards=False,
                            MatchSoundsLike= False, MatchAllWordForms=False,Forward=False,Wrap = 1,Format = False,
                            ReplaceWith = strnew,Replace=2,MatchKashida=False,MatchDiacritics=False,
                            MatchAlefHamza=False,MatchControl=False)
                doc.SaveAs(targetfile)   # 需要保存才可以保留替换结果，如果想在原文件上修改可以使用doc.Save()方法
                doc.Close(False)  # 关闭文件
            except Exception as e:
                errmark = True  # 标记是否出错的变量
                print(e)
        w.Quit(constants.wdDoNotSaveChanges)  # 关闭Word应用程序
        if not errmark:  # 不出错时
            print("替换完毕！文件路径：",targetpath)
    except TypeError as e:
        print('出错了！')
        print(e)
if __name__ == '__main__':
    filelist =[os.path.abspath("test\\demo.docx"),os.path.abspath("test\\demo1.docx")]
    targetpath = os.path.abspath("new")  # 指定目标路径为当前项目根目录\new目录
    strold = u"python"  # 要替换的字符串
    strnew = u"Python"   # 替换为的字符串
    replaceall(filelist,targetpath,strold,strnew)  # 替换Word文档中的指定内容
