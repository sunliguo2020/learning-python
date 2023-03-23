# -*- coding:utf-8 -*-
import os  # 导入系统功能模块
from win32com.client import Dispatch, DispatchEx  # 导入pywin32模块的client包下的函数
from win32com.client import constants  #  导入pywin32模块的client包下的保存COM常量的类
from win32com.client import gencache    #  导入pywin32模块的client包下的gencache函数
import re  # 导入正则表达式模块


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
                elif os.path.splitext(fi_d)[1] == file_ext:  # 要获取除了Word文件以外的文件
                    filelist_out.append(fi_d)  # 将文件路径添加到路径列表中
                else:
                    pass
        filelist_out.sort()  # 对路径进行排序
    return filelist_out  # 返回文件完整路径列表

'''Word转换为PDF(多个文件)
   filelist：在转换的Word文件列表
   targetpath：输出目录
   digit：格式化数字编号的位数，如指定为4表示生成0001、0002格式的编号
'''
def wordtopdf(filelist,targetpath,digit):
    valueList = []
    try:
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
        # 开始转换
        w = Dispatch("Word.Application")
        for index,fullfilename in enumerate(filelist):
            (filepath,filename) = os.path.split(fullfilename)  # 分割文件路径和文件名，其中，filepath表示文件路径；filename表示文件名
            softfilename = os.path.splitext(filename)  # 分割文件名和扩展名
            os.chdir(filepath)  
            doc = os.path.abspath(filename)
            os.chdir(targetpath)
            pdfname = str(index).zfill(digit) + ".pdf"
            output = os.path.abspath(pdfname)
            pdf_name = output

            # 文档路径需要为绝对路径，因为Word启动后当前路径不是调用脚本时的当前路径。
            try: # 捕捉异常
                doc = w.Documents.Open(doc, ReadOnly=1)
                doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF, 
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
            except Exception as e: # 处理异常
                print(e)
            if os.path.isfile(pdf_name): # 判断文件是否存在
                valueList.append(pdf_name) # 添加到文件列表中
            else:
                print('转换失败！')
                return False
        w.Quit(constants.wdDoNotSaveChanges) # 退出Word应用程序
        return valueList  # 返回生成PDF文件列表
    except TypeError as e:
        print('出错了！')
        print(e)
        return False
if __name__ == '__main__':
    sourcepath = r"E:/learn/test/doc/temp"  # 指定源路径（Word文档所在路径）
    targetpath = r"E:/learn/test/doc/pdf/"  # 指定目标路径（PDF保存路径）
    filelist = getfilenames(sourcepath,[],'.doc')  # 获取Word文档路径
    valueList = wordtopdf(filelist,targetpath,4)  # 实现将Word文档批量转换为PDF
    if valueList:
        print("转换成功")
    else:
        print("没有要转换的Word文档或者转换失败！")

