# -*- coding:utf-8 -*-
import os  # 导入系统功能模块
from win32com.client import Dispatch, DispatchEx  # 导入pywin32模块的client包下的函数
from win32com.client import constants  #  导入pywin32模块的client包下的保存COM常量的类
from win32com.client import gencache    #  导入pywin32模块的client包下的gencache函数
from PyPDF2 import  PdfFileReader  # 获取页码用
import re  # 导入正则表达式模块

import pythoncom  # 导入封装了OLE自动化API的模块，该模块为pywin32的子模块


'''获取指定目录下的文件
   filepath：要遍历的目录
   filelist_out：输出文件列表
   file_ext：文件的扩展名，默认为任何类型的文件
'''
def getfilenames(filepath='',filelist_out=[],file_ext='all'):
    # 遍历filepath下的所有文件，包括子目录下的文件
    for fpath, dirs, fs in os.walk(filepath):
        for f in fs:
            fi_d = os.path.join(fpath, f)
            if file_ext == '.doc':  # 遍历Word文档文件
                if os.path.splitext(fi_d)[1] in ['.doc','.docx']:   # 判断是否为Word文件
                    filelist_out.append(re.sub(r'\\','/',fi_d))  # 添加到路径列表中
            else:
                if  file_ext == 'all':  # 要获取所有文件的情况
                    filelist_out.append(fi_d)  # 将文件路径添加到路径列表中
                elif os.path.splitext(fi_d)[1] == file_ext:  # 要获取除了Wrod文件以外的文件
                    filelist_out.append(fi_d)  # 将文件路径添加到路径列表中
                else:
                    pass
        filelist_out.sort()  # 对路径进行排序
    return filelist_out  # 返回文件完整路径列表

# Word转换为PDF(多个文件)
def wordtopdf(filelist,targetpath):
    totalPages = 0   # 记录总页码
    valueList = []
    try:
        pythoncom.CoInitialize()   # 调用线程初始化COM库，解决调用Word 2007时出现“尚未调用CoInitialize”错误的问题
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        # 开始转换
        w = Dispatch("Word.Application")
        for fullfilename in filelist:
            (filepath,filename) = os.path.split(fullfilename)  # 分割文件路径和文件名，其中，filepath表示文件路径；filename表示文件名
            softfilename = os.path.splitext(filename)  # 分割文件名和扩展名
            os.chdir(filepath)  
            doc = os.path.abspath(filename)
            os.chdir(targetpath)
            pdfname = softfilename[0] + ".pdf"
            output = os.path.abspath(pdfname)
            pdf_name = output

            # 文档路径需要为绝对路径，因为Word启动后当前路径不是调用脚本时的当前路径。
            try: # 捕捉异常
                doc = w.Documents.Open(doc, ReadOnly=1)
                doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF, \
                                        Item=constants.wdExportDocumentWithMarkup,
                                        CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            except Exception as e: # 处理异常
                print(e)
            if os.path.isfile(pdf_name): # 判断文件是否存在
                # 获取页码
                pages = getPdfPageNum(pdf_name)   # 获取页码
                valueList.append([fullfilename,str(pages)])
                totalPages += pages  # 累加页码
                os.remove(pdf_name)  # 删除生成的PDF文件
            else:
                print('转换失败！')
                return False
        w.Quit(constants.wdDoNotSaveChanges) # 退出Word应用程序
        return totalPages,valueList  # 返回总页码和每个文档的页码
    except TypeError as e:
        print('出错了！')
        print(e)
        return False
'''
功能：统计文档页码
path：文件绝对路径
'''
def getPdfPageNum(path):
    with open(path, "rb") as file:
        doc = PdfFileReader(file)
        pagecount = doc.getNumPages()
    return pagecount

if __name__ == '__main__':
    sourcepath = r"E:/learn/test/doc/temp"  # 指定源路径（Word文档所在路径）
    targetpath = r"E:/learn/test/doc/pdf/"  # 指定目标路径（PDF保存路径）
    filelist = getfilenames(sourcepath,[],'.doc')  # 获取Word文档路径
    valueList = wordtopdf(filelist,targetpath)  # 实现将Word文档批量转换为PDF
    resultList = valueList[1]  # 获取统计结果
    if valueList:
        for i in resultList:
            print(i[0],i[1])
        totalPages = str(valueList[0]) # 总页数
        print("合计页数：",totalPages)
    else:
        print("没有要统计的文件或者统计失败！")


