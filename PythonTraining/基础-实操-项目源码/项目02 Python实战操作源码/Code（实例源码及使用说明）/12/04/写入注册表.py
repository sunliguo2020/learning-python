import win32api # 需要安装win32com模块，命令为：pip install pywin32
import win32con  # 导入win32con模块，该模块包含在win32com中
 
name = 'auto run python' # 要添加的项值名称（支持中文）
path = r'E:\exe.bat' # 要执行程序的绝对路径
# 注册表项名
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# 异常处理
try:
    # 打开键
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)  # 打开键
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)  # 写入键值
    win32api.RegCloseKey(key)  # 关闭键
except Exception as e:
    print('error',e)   # 输出异常信息
else:
    print('添加成功！')
