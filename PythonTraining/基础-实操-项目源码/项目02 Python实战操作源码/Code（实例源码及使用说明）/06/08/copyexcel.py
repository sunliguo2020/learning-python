from win32com.client import Dispatch # 导入win32com模块
import os  # 导入操作系统模块
'''
复制Sheet页到另一个Excel文件
   filepath：要遍历的目录
   filelist：要复制的Excel文件列表
   targetfilename：新生成的Excel文件的名称
'''
def copysheet(filepath, filelist,targetfilename):
    excelapp = Dispatch('Excel.Application') # 创建Excel应用对象
    excelapp.visible = 1 # 此行设置打开的Excel表格为可见状态；忽略则Excel表格默认不可见
    targetfile = excelapp.Workbooks.Add() #新建Excel文件
    targetws_list = targetfile.Worksheets
    for filename in filelist:   # 遍历Excel文件列表
        filesplit = filename.split('.')
        if filesplit[-1] == 'xlsx' or filesplit[-1] == 'xls':  # 判断是否为Excel文件
            excelfile = excelapp.Workbooks.Open(filepath + '\\' + filename)  # 打开一个Sheet页
            ws = excelfile.Worksheets
            ws.Copy(None,targetws_list(1)) #跨表复制,插入到第一个Sheet页之后
            excelfile.Close(SaveChanges=1)
        else:
            pass # 占位符，不执行操作
    targetws_list[0].Delete()  # 删除默认创建的Sheet1
    targetfile.SaveAs(filepath + targetfilename)  # 保存Sheet页到新Excel文件中
    targetfile.Close(SaveChanges=1)  # 关闭Excel文件
    excelapp.quit()    # 退出Excel应用对象
'''获取指定目录下的文件
   filepath：要遍历的目录
   filelist_out：输出文件列表
   file_ext：文件的扩展名，默认为任何类型的文件
'''
def getfilenames(filepath='',filelist_out=[],file_ext='all'):
    # 遍历filepath下的文件
    for filename in os.listdir(filepath):
        if file_ext == '.xlsx':  # 遍历Word文档文件
            if os.path.splitext(filename)[1] in ['.xlsx','.xls']:
                filelist_out.append(filename) # 添加到路径列表中
        else:
            if  file_ext == 'all':  # 遍历全部文件
                filelist_out.append(filename) # 添加到路径列表中
            elif os.path.splitext(filename)[1] == file_ext:
                filelist_out.append(filename)  # 添加到路径列表中
            else:
                pass
    filelist_out.sort(reverse=True)  # 对列表进行排序
    return filelist_out  # 返回文件完整路径列表

if __name__ == '__main__':
    filepath = r"G:\开发二部\周工作总结\2019\2019-04-22~2019-04-26\杂\新建文件夹"  # Excel文件保存的路径
    copysheet(filepath, getfilenames(filepath, [], '.xlsx'), r'\周工作总结.xlsx')  # 合并多个Sheet页



