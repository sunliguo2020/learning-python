# -*- coding:utf-8 -*-
import os  # 导入系统功能模块
from win32com.client import Dispatch, DispatchEx  # 导入pywin32模块的client包下的函数
from win32com.client import constants  #  导入pywin32模块的client包下的保存COM常量的类
from win32com.client import gencache    #  导入pywin32模块的client包下的gencache函数
import re  # 导入正则表达式模块

import sys, codecs   # 导入标准模块
from PyPDF2 import PdfFileReader, PdfFileMerger   # 导入第三方模块PyPDF2

'''
   合并pdf文件，输出的pdf文件按输入的pdf文件名生成书签
'''
def mergefiles(path, output_filename, import_bookmarks=False):
    ''' 遍历目录下的所有pdf将其合并输出到一个pdf文件中， # 返回数字（将按该数字排序）输出的pdf文件默认带书签，
    书签名为之前的文件名。默认情况下原始文件的书签不会导入，使用import_bookmarks=True可以将原文件所带的书签也
    导入到输出的PDF文件中
    '''
    merger = PdfFileMerger() # 创建PDF合并对象
    filelist = getfilenames(filepath=path,filelist_out=[], file_ext='.pdf')  # 获取要合并的PDF文件
    if len(filelist) == 0:  # 判断是否存在要合并的文件
        print("当前目录及子目录下不存在pdf文件")
        sys.exit()  # 退出文件系统
    for filename in filelist:  # 遍历文件列表
        f = codecs.open(filename, 'rb') # 使用codecs的open()方法打开文件时，会自动转换为内部Unicode编码
        file_rd = PdfFileReader(f)
        short_filename = os.path.basename(os.path.splitext(filename)[0]) # 获取文件名称（不包括文件路径）
        if file_rd.isEncrypted == True:
            print('不支持的加密文件：%s'%(filename))
            continue
        merger.append(file_rd, bookmark=short_filename, import_bookmarks=import_bookmarks)
        f.close()  # 关闭文件对象
    out_filename=os.path.join(os.path.abspath(path), output_filename)  # 将文件名和路径连接为一个完整路径
    merger.write(out_filename) # 写入内容
    merger.close()  # 关闭PDF合并对象

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


'''
功能：提取目录并保存到新的Word文档中
pdfpath：合并后的PDF文件绝对路径，包括文件名
listpath：目标路径
isPage：是否包含页码
'''
def getPdfOutlines(pdfpath,listpath,isPage,level):
    with open(pdfpath, "rb") as file:
        doc = PdfFileReader(file)
        outlines = doc.getOutlines()  # 获取大纲
        global returnlist  # 全局变量，保存大纲的列表
        returnlist = []   # 创建一个空列表
        mylist = getOutline(outlines,isPage,level)  # 递归获取大纲
        w = DispatchEx("Word.Application")  # 创建Word文档应用程序对象
        w.Visible = 1
        w.DisplayAlerts = 0
        doc1 = w.Documents.Add()# 添加一个Word文档对象
        range1 = doc1.Range(0,0)
        for item in mylist:       # 通过循环将获取的目录列表插入到Word文档对象中
             range1.InsertAfter(item)
        outpath = os.path.join(listpath,'list.docx') # 连接Word文档路径

        doc1.SaveAs(outpath)  # 保存文件
        doc1.Close()  # 关闭Word文档对象
        w.Quit()  # 退出Word文档应用程序对象
    return outpath

'''
功能：提取指定层级的大纲
obj：Word文档的大纲对象
isPage：是否包含页码
selectLevel：目录层级，值为0~3的数。0表示全部大纲、1表示一级大纲……

'''
def getOutline(obj,isList,selectLevel):  # 获取指定层级的大纲
    global returnlist
    if selectLevel == 0:            # 获取全部大纲
        returnlist = getAllOutline(obj,isList)   # 递归获取全部大纲
    else:
        for o in obj:
            if selectLevel == 1:  # 只提取一级标题
                if type(o).__name__ == 'Destination':
                    isPage(o, isList)  # 输出大纲内容（处理是否包含页码）
            elif selectLevel == 2:  # 提取到二级标题
                if type(o).__name__ == 'Destination':
                    isPage(o, isList)  # 输出大纲内容（处理是否包含页码）
                elif type(o).__name__ == 'list':
                    getOne(o, isList)
            elif selectLevel == 3:      # 提取到三级标题
                if type(o).__name__ == 'Destination':
                    isPage(o, isList)  # 输出大纲内容（处理是否包含页码）
                elif type(o).__name__ == 'list':
                    for o1 in o:
                        if type(o1).__name__ == 'Destination':
                            isPage(o1, isList)  # 输出大纲内容（处理是否包含页码）
                        elif type(o1).__name__ == 'list':
                            getOne(o1, isList)
    return returnlist
def getOne(obj,isList):  # 获取当前一级大纲
    for o in obj:
        if type(o).__name__ == 'Destination':
            isPage(o, isList)  # 输出大纲内容（处理是否包含页码）
    return returnlist
# 输出大纲内容（处理是否包含页码）
def isPage(o,isList):
    if isList:  # 包括页码
        returnlist.append(o.get('/Title') + "\t\t" + str(o.get('/Page') + 1) + "\n")
    else:  # 不包括页码
        returnlist.append(o.get('/Title') + "\n")

# Word转换为PDF(多个文件)
def wordtopdf(filelist,targetpath):
    valueList = []
    try:
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
    valueList = wordtopdf(filelist,targetpath)  # 实现将Word文档批量转换为PDF
    if valueList:
        # 将多个PDF文件合并为一个PDF文件
        mergefiles(targetpath, 'merged.pdf', True)
        temp = [os.path.join(targetpath , 'merged.pdf')] # 组合PDF文件路径
        for file in valueList:            # 遍历临时生成的PDF文件列表
            os.remove(file)                # 删除PDF文件
        resultvalue = getPdfOutlines(temp[0], targetpath, True,2)  # 提取目录
        os.remove(temp[0])  # 删除合并后的PDF文件
        print("提取完成！文件保存在：",targetpath )
    else:
        print("没有要提取目录的Word文档或者提取失败！")
	


